from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.anthropic import Claude
from agno.models.google import Gemini
from agno.models.groq import Groq
from typing import Optional, List

class ListingAgent:
    """Agent for creating and optimizing marketplace listings."""
    
    def __init__(self, model_provider: str = "openai"):
        self.model_provider = model_provider
        self.agent = self._create_agent()
    
    def _create_agent(self) -> Agent:
        """Create the listing agent with specified model provider."""
        
        if self.model_provider == "openai":
            model = OpenAIChat(id="gpt-4o-mini")
        elif self.model_provider == "anthropic":
            model = Claude(id="claude-3-haiku-20240307")
        elif self.model_provider == "google":
            model = Gemini(id="gemini-2.0-flash-exp")
        elif self.model_provider == "groq":
            model = Groq(id="llama-3.3-70b-versatile")
        else:
            raise ValueError(f"Unknown model provider: {self.model_provider}")
        
        return Agent(
            model=model,
            name="Marketplace Listing Expert",
            description="An AI assistant specialized in creating and optimizing marketplace listings",
            instructions=[
                "You are an expert in creating compelling marketplace listings.",
                "Help users create engaging product titles, descriptions, and optimize listings for better visibility.",
                "Provide actionable suggestions for keywords, pricing strategies, and listing improvements.",
                "Consider SEO best practices and marketplace algorithms.",
                "Be professional, concise, and results-oriented in your responses."
            ],
            markdown=True,
            show_tool_calls=True,
        )
    
    def create_listing(self, product_info: dict) -> str:
        """Create a complete marketplace listing from product information."""
        
        prompt = f"""
        Create a compelling marketplace listing for the following product:
        
        Product Information:
        - Name: {product_info.get('name', '')}
        - Category: {product_info.get('category', '')}
        - Description: {product_info.get('description', '')}
        - Features: {', '.join(product_info.get('features', []))}
        - Target Audience: {product_info.get('target_audience', '')}
        - Price Range: {product_info.get('price_range', '')}
        
        Please provide:
        1. An attention-grabbing title
        2. A detailed product description
        3. Key features/benefits bullet points
        4. Suggested keywords/tags
        5. Pricing recommendations
        6. Any additional optimization tips
        """
        
        response = self.agent.run(prompt)
        return response.content
    
    def optimize_title(self, current_title: str, product_category: str) -> str:
        """Optimize an existing product title for better visibility."""
        
        prompt = f"""
        Optimize this product title for better marketplace visibility:
        
        Current Title: {current_title}
        Product Category: {product_category}
        
        Please provide:
        1. An optimized title that's more searchable
        2. Explanation of the improvements made
        3. Alternative title suggestions
        """
        
        response = self.agent.run(prompt)
        return response.content
    
    def generate_keywords(self, product_description: str, category: str) -> List[str]:
        """Generate relevant keywords for a product listing."""
        
        prompt = f"""
        Generate a list of relevant keywords for this product:
        
        Product Description: {product_description}
        Category: {category}
        
        Please provide:
        1. Primary keywords (high search volume)
        2. Long-tail keywords (more specific)
        3. Seasonal keywords (if applicable)
        4. Competitor keywords to consider
        
        Return as a comma-separated list.
        """
        
        response = self.agent.run(prompt)
        keywords = [kw.strip() for kw in response.content.split(',')]
        return keywords