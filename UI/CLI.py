# main.py
from  app.agent import ProductResearchAgent
import json

def main():
    # Initialize the agent
    agent = ProductResearchAgent()
    
    # Example usage
    query = "Best wireless headphones for working from home under $200"
    
    print("🔍 Starting product research...")
    print(f"Query: {query}\n")
    
    # Run the research
    results = agent.research_product(query)
    
    # Display results
    print("=" * 60)
    print("📊 PRODUCT RESEARCH RESULTS")
    print("=" * 60)
    
    print("\n🎯 USER NEEDS ANALYSIS:")
    print(results["user_needs"])
    
    print("\n📈 ANALYSIS:")
    print(results["analysis"])
    
    print("\n💡 RECOMMENDATIONS:")
    print(results["recommendations"])
    
    print("\n📋 COMPARISON CHART:")
    print(results["comparison_chart"])
    
    # Save results to file
    with open("research_results.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Results saved to 'data/Research_results.json'")

if __name__ == "__main__":
    main()

