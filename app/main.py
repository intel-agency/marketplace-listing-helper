from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add the parent directory to the path so we can import our agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.listing_agent import ListingAgent

app = FastAPI(
    title="Marketplace Listing Helper API",
    description="AI-powered marketplace listing optimization tool",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ProductInfo(BaseModel):
    name: str
    category: str
    description: str
    features: List[str]
    target_audience: Optional[str] = ""
    price_range: Optional[str] = ""

class TitleOptimizationRequest(BaseModel):
    current_title: str
    product_category: str

class KeywordsRequest(BaseModel):
    product_description: str
    category: str

class ListingResponse(BaseModel):
    listing: str
    model_used: str

class TitleOptimizationResponse(BaseModel):
    optimized_title: str
    explanation: str
    alternatives: List[str]
    model_used: str

class KeywordsResponse(BaseModel):
    keywords: List[str]
    model_used: str

# Initialize the agent
agent = ListingAgent(model_provider="openai")

@app.get("/")
async def root():
    return {"message": "Marketplace Listing Helper API", "version": "0.1.0"}

@app.post("/create-listing", response_model=ListingResponse)
async def create_listing(product_info: ProductInfo):
    try:
        listing = agent.create_listing(product_info.dict())
        return ListingResponse(listing=listing, model_used="openai")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/optimize-title", response_model=TitleOptimizationResponse)
async def optimize_title(request: TitleOptimizationRequest):
    try:
        result = agent.optimize_title(request.current_title, request.product_category)
        # Parse the result to extract title, explanation, and alternatives
        lines = result.split('\n')
        optimized_title = ""
        explanation = ""
        alternatives = []
        
        for line in lines:
            if "optimized title" in line.lower() and not optimized_title:
                optimized_title = line.split(':', 1)[1].strip() if ':' in line else line
            elif "improvement" in line.lower() and not explanation:
                explanation = line.split(':', 1)[1].strip() if ':' in line else line
            elif "alternative" in line.lower():
                alt = line.split(':', 1)[1].strip() if ':' in line else line
                if alt:
                    alternatives.append(alt)
        
        return TitleOptimizationResponse(
            optimized_title=optimized_title or request.current_title,
            explanation=explanation or "Title optimized for better search visibility",
            alternatives=alternatives[:3],  # Limit to 3 alternatives
            model_used="openai"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-keywords", response_model=KeywordsResponse)
async def generate_keywords(request: KeywordsRequest):
    try:
        keywords = agent.generate_keywords(request.product_description, request.category)
        return KeywordsResponse(keywords=keywords[:20], model_used="openai")  # Limit to 20 keywords
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "openai"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)