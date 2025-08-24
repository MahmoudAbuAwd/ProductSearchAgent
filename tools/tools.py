# tools.py
from tavily import TavilyClient
from typing import List, Dict
import json
import pandas as pd
from config import Config

class ProductSearchTools:
    def __init__(self):
        self.tavily = TavilyClient(api_key=Config.TAVILY_API_KEY)
    
    def search_product_reviews(self, product_name: str, max_results: int = 5) -> str:
        """Search for product reviews and ratings"""
        try:
            query = f"{product_name} reviews ratings pros cons"
            results = self.tavily.search(
                query=query,
                search_depth="advanced",
                max_results=max_results
            )
            
            formatted_results = []
            for result in results.get('results', []):
                formatted_results.append({
                    'title': result.get('title', ''),
                    'content': result.get('content', ''),
                    'url': result.get('url', ''),
                    'score': result.get('score', 0)
                })
            
            return json.dumps(formatted_results, indent=2)
        except Exception as e:
            return f"Error searching reviews: {str(e)}"
    
    def search_product_prices(self, product_name: str, max_results: int = 5) -> str:
        """Search for product prices across different retailers"""
        try:
            query = f"{product_name} price buy online retailer comparison"
            results = self.tavily.search(
                query=query,
                search_depth="advanced",
                max_results=max_results
            )
            
            formatted_results = []
            for result in results.get('results', []):
                formatted_results.append({
                    'title': result.get('title', ''),
                    'content': result.get('content', ''),
                    'url': result.get('url', ''),
                    'score': result.get('score', 0)
                })
            
            return json.dumps(formatted_results, indent=2)
        except Exception as e:
            return f"Error searching prices: {str(e)}"
    
    def search_product_comparisons(self, product1: str, product2: str, max_results: int = 3) -> str:
        """Search for comparisons between two products"""
        try:
            query = f"{product1} vs {product2} comparison review differences"
            results = self.tavily.search(
                query=query,
                search_depth="advanced",
                max_results=max_results
            )
            
            formatted_results = []
            for result in results.get('results', []):
                formatted_results.append({
                    'title': result.get('title', ''),
                    'content': result.get('content', ''),
                    'url': result.get('url', ''),
                    'score': result.get('score', 0)
                })
            
            return json.dumps(formatted_results, indent=2)
        except Exception as e:
            return f"Error searching comparisons: {str(e)}"
