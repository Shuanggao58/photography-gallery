from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Category(BaseModel):
    """Category model for organizing photos (e.g., Portrait, Landscape, Wedding)"""
    __tablename__ = "categories"
    
    # Basic info
    name = Column(String(100), unique=True, index=True, nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    
    # Display settings
    color = Column(String(7), nullable=True)  # Hex color code
    icon = Column(String(50), nullable=True)  # Icon name
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    
    # SEO
    meta_title = Column(String(255), nullable=True)
    meta_description = Column(Text, nullable=True)
    
    # Relationships
    photos = relationship("Photo", back_populates="category")
    
    def __repr__(self):
        return f"<Category(name={self.name}, slug={self.slug})>"
