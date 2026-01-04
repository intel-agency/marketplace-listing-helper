#!/usr/bin/env python3
"""
Basic usage example for the Marketplace Listing Helper
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.listing_agent import ListingAgent

def main():
    """Demonstrate basic usage of the listing agent."""
    
    # Initialize the agent with OpenAI
    agent = ListingAgent(model_provider="openai")
    
    # Example product information
    product_info = {
        "name": "Vintage Leather Handbag",
        "category": "Fashion Accessories",
        "description": "Beautiful vintage leather handbag in excellent condition. Features brass hardware and multiple compartments.",
        "features": ["Genuine leather", "Brass hardware", "Multiple compartments", "Vintage style", "Excellent condition"],
        "target_audience": "Fashion-conscious women aged 25-55",
        "price_range": "$50-$100"
    }
    
    print("🚀 Creating marketplace listing...")
    print("=" * 50)
    
    # Create a complete listing
    listing = agent.create_listing(product_info)
    print("Generated Listing:")
    print(listing)
    print("\n" + "=" * 50)
    
    # Optimize a title
    current_title = "Old Leather Bag"
    optimized = agent.optimize_title(current_title, "Fashion Accessories")
    print(f"Title Optimization for '{current_title}':")
    print(optimized)
    print("\n" + "=" * 50)
    
    # Generate keywords
    keywords = agent.generate_keywords(
        "Beautiful vintage leather handbag in excellent condition with brass hardware",
        "Fashion Accessories"
    )
    print("Generated Keywords:")
    print(", ".join(keywords))

if __name__ == "__main__":
    main()