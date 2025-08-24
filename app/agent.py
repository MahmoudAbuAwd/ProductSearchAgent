# agent.py
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, List, Dict, Any
import json
from tools.tools import ProductSearchTools
from config import Config

# Configure Gemini
genai.configure(api_key=Config.GEMINI_API_KEY)

class ProductResearchState(TypedDict):
    query: str
    user_needs: str
    search_results: Dict[str, Any]
    analysis: str
    recommendations: str
    comparison_chart: str
    messages: List[Any]

class ProductResearchAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=Config.GEMINI_MODEL,
            google_api_key=Config.GEMINI_API_KEY,
            temperature=0.3
        )
        self.tools = ProductSearchTools()
        self.graph = self._build_graph()
    
    def _build_graph(self) -> StateGraph:
        """Build the LangGraph workflow"""
        graph = StateGraph(ProductResearchState)
        
        # Add nodes
        graph.add_node("understand_query", self._understand_query)
        graph.add_node("search_reviews", self._search_reviews)
        graph.add_node("search_prices", self._search_prices)
        graph.add_node("analyze_data", self._analyze_data)
        graph.add_node("generate_recommendations", self._generate_recommendations)
        graph.add_node("create_comparison", self._create_comparison)
        
        # Add edges
        graph.add_edge("understand_query", "search_reviews")
        graph.add_edge("search_reviews", "search_prices")
        graph.add_edge("search_prices", "analyze_data")
        graph.add_edge("analyze_data", "generate_recommendations")
        graph.add_edge("generate_recommendations", "create_comparison")
        graph.add_edge("create_comparison", END)
        
        # Set entry point
        graph.set_entry_point("understand_query")
        
        return graph.compile()
    
    def _understand_query(self, state: ProductResearchState) -> ProductResearchState:
        """Understand user query and extract product information"""
        query = state["query"]
        
        prompt = f"""
        Analyze this product research query: "{query}"
        
        Extract:
        1. Main product(s) being researched
        2. User's specific needs/requirements
        3. Budget constraints (if mentioned)
        4. Use case or purpose
        
        Return as JSON format with keys: product, needs, budget, use_case
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        try:
            parsed = json.loads(response.content)
            state["user_needs"] = json.dumps(parsed)
        except:
            state["user_needs"] = response.content
        
        return state
    
    def _search_reviews(self, state: ProductResearchState) -> ProductResearchState:
        """Search for product reviews"""
        user_needs = json.loads(state["user_needs"]) if state["user_needs"].startswith('{') else {"product": state["query"]}
        product = user_needs.get("product", state["query"])
        
        reviews = self.tools.search_product_reviews(product)
        
        if "search_results" not in state:
            state["search_results"] = {}
        state["search_results"]["reviews"] = reviews
        
        return state
    
    def _search_prices(self, state: ProductResearchState) -> ProductResearchState:
        """Search for product prices"""
        user_needs = json.loads(state["user_needs"]) if state["user_needs"].startswith('{') else {"product": state["query"]}
        product = user_needs.get("product", state["query"])
        
        prices = self.tools.search_product_prices(product)
        state["search_results"]["prices"] = prices
        
        return state
    
    def _analyze_data(self, state: ProductResearchState) -> ProductResearchState:
        """Analyze collected data using Gemini"""
        reviews = state["search_results"].get("reviews", "")
        prices = state["search_results"].get("prices", "")
        user_needs = state["user_needs"]
        
        prompt = f"""
        Analyze this product research data:
        
        User Needs: {user_needs}
        
        Reviews Data: {reviews}
        
        Prices Data: {prices}
        
        Provide a comprehensive analysis including:
        1. Key pros and cons
        2. Price range analysis
        3. User sentiment summary
        4. Quality indicators
        5. Value for money assessment
        
        Format as structured analysis.
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        state["analysis"] = response.content
        
        return state
    
    def _generate_recommendations(self, state: ProductResearchState) -> ProductResearchState:
        """Generate personalized recommendations"""
        analysis = state["analysis"]
        user_needs = state["user_needs"]
        
        prompt = f"""
        Based on this analysis: {analysis}
        And user needs: {user_needs}
        
        Generate specific recommendations:
        1. Should they buy this product? Why or why not?
        2. Best retailer/price point
        3. Alternative products to consider
        4. Key factors to watch out for
        5. Best time to buy (if applicable)
        
        Make it actionable and personalized.
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        state["recommendations"] = response.content
        
        return state
    
    def _create_comparison(self, state: ProductResearchState) -> ProductResearchState:
        """Create comparison chart/summary"""
        analysis = state["analysis"]
        recommendations = state["recommendations"]
        
        prompt = f"""
        Create a structured comparison summary based on:
        Analysis: {analysis}
        Recommendations: {recommendations}
        
        Format as:
        ## Product Summary
        - **Overall Score**: X/10
        - **Best For**: [use case]
        - **Price Range**: $X - $Y
        - **Top Pros**: [list]
        - **Main Cons**: [list]
        - **Recommendation**: [buy/wait/consider alternatives]
        
        ## Quick Decision Matrix
        | Criteria | Score | Notes |
        |----------|--------|-------|
        | Value | X/5 | ... |
        | Quality | X/5 | ... |
        | Features | X/5 | ... |
        """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        state["comparison_chart"] = response.content
        
        return state
    
    def research_product(self, query: str) -> Dict[str, Any]:
        """Main method to research a product"""
        initial_state = ProductResearchState(
            query=query,
            user_needs="",
            search_results={},
            analysis="",
            recommendations="",
            comparison_chart="",
            messages=[]
        )
        
        final_state = self.graph.invoke(initial_state)
        
        return {
            "query": final_state["query"],
            "user_needs": final_state["user_needs"],
            "analysis": final_state["analysis"],
            "recommendations": final_state["recommendations"],
            "comparison_chart": final_state["comparison_chart"],
            "raw_data": final_state["search_results"]
        }
