"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Marketing agency specific schemas

class Lead(BaseModel):
    """
    Leads captured from website forms
    Collection name: "lead"
    """
    name: str = Field(..., description="Contact full name")
    email: str = Field(..., description="Contact email")
    company: Optional[str] = Field(None, description="Company name")
    website: Optional[str] = Field(None, description="Company website")
    phone: Optional[str] = Field(None, description="Phone number")
    services: Optional[List[str]] = Field(default=None, description="Interested services")
    budget: Optional[str] = Field(None, description="Estimated monthly budget range")
    message: Optional[str] = Field(None, description="Additional details or goals")
    source: Optional[str] = Field("website", description="Lead source e.g. website, referral")

class CaseStudy(BaseModel):
    """
    Case studies/portfolio entries
    Collection name: "casestudy"
    """
    title: str
    client: str
    industry: Optional[str] = None
    summary: str
    impact: Optional[str] = None
    metrics: Optional[dict] = None
    image_url: Optional[str] = None
    slug: Optional[str] = None

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
