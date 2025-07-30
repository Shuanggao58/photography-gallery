from sqlalchemy import Column, String, Text, Boolean, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Tag(BaseModel):
    """Tag model for flexible photo tagging system"""
    __tablename__ = "tags"
    
    # Basic info
    name = Column(String(50), unique=True, index=True, nullable=False)
    slug = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    
    # Display settings
    color = Column(String(7), nullable=True)  # Hex color code
    is_active = Column(Boolean, default=True)
    usage_count = Column(Integer, default=0)  # Cache for performance
    
    # Relationships (many-to-many with photos defined in associations)
    # photos relationship will be defined via association table
    
    def __repr__(self):
        return f"<Tag(name={self.name}, usage_count={self.usage_count})>"
