from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
from app.models.associations import album_photos
import enum

class AlbumVisibility(enum.Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    UNLISTED = "unlisted"  # Accessible via direct link only

class Album(BaseModel):
    """Album model for organizing photos into collections"""
    __tablename__ = "albums"
    
    # Basic info
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    
    # Display settings
    visibility = Column(SQLEnum(AlbumVisibility), default=AlbumVisibility.PUBLIC, index=True)
    is_featured = Column(Boolean, default=False)
    sort_order = Column(Integer, default=0)
    
    # Cover photo
    cover_photo_id = Column(Integer, ForeignKey('photos.id', ondelete='SET NULL'), nullable=True)
    
    # SEO
    meta_title = Column(String(255), nullable=True)
    meta_description = Column(Text, nullable=True)
    
    # Statistics
    view_count = Column(Integer, default=0)
    photo_count = Column(Integer, default=0)  # Cache for performance
    
    # Foreign keys
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships
    owner = relationship("User", back_populates="albums")
    cover_photo = relationship("Photo", foreign_keys=[cover_photo_id])
    photos = relationship(
        "Photo", 
        secondary=album_photos, 
        backref="albums",
        order_by="album_photos.c.sort_order"
    )
    
    def __repr__(self):
        return f"<Album(title={self.title}, visibility={self.visibility.value}, photo_count={self.photo_count})>"
    
    @property
    def cover_image_url(self):
        """Return cover photo URL or first photo in album"""
        if self.cover_photo:
            return self.cover_photo.url
        elif self.photos:
            return self.photos[0].url
        return None
