from sqlalchemy import Column, String, Text, Boolean, Integer, ForeignKey, Float, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from app.models.base import BaseModel
from app.models.associations import photo_tags
import enum

class PhotoStatus(enum.Enum):
    UPLOADING = "uploading"
    PROCESSING = "processing" 
    PUBLISHED = "published"
    DRAFT = "draft"
    ARCHIVED = "archived"

class Photo(BaseModel):
    """Photo model - main entity for the photography gallery"""
    __tablename__ = "photos"
    
    # Basic info
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    alt_text = Column(String(255), nullable=True)  # For accessibility
    
    # File information
    original_filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)  # S3 key or file path
    file_size = Column(Integer, nullable=False)  # File size in bytes
    mime_type = Column(String(100), nullable=False)
    
    # Image dimensions
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    aspect_ratio = Column(Float, nullable=True)  # Calculated field
    
    # Processing status
    status = Column(SQLEnum(PhotoStatus), default=PhotoStatus.PROCESSING, index=True)
    is_featured = Column(Boolean, default=False)
    is_public = Column(Boolean, default=True)
    
    # Image variants (thumbnails, different sizes)
    thumbnails = Column(JSON, nullable=True)  # Store different size URLs
    
    # EXIF and camera data
    exif_data = Column(JSON, nullable=True)  # Raw EXIF data
    camera_make = Column(String(100), nullable=True)
    camera_model = Column(String(100), nullable=True)
    lens = Column(String(100), nullable=True)
    focal_length = Column(String(20), nullable=True)
    aperture = Column(String(10), nullable=True)
    shutter_speed = Column(String(20), nullable=True)
    iso = Column(Integer, nullable=True)
    taken_at = Column(String(50), nullable=True)  # Date photo was taken
    
    # Location data
    location_name = Column(String(255), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    # SEO and metadata
    meta_title = Column(String(255), nullable=True)
    meta_description = Column(Text, nullable=True)
    keywords = Column(String(500), nullable=True)
    
    # Statistics
    view_count = Column(Integer, default=0)
    download_count = Column(Integer, default=0)
    like_count = Column(Integer, default=0)
    
    # Display settings
    sort_order = Column(Integer, default=0)
    
    # Foreign keys
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    
    # Relationships
    owner = relationship("User", back_populates="photos")
    category = relationship("Category", back_populates="photos")
    tags = relationship("Tag", secondary=photo_tags, backref="photos")
    # albums relationship defined in Album model
    
    def __repr__(self):
        return f"<Photo(title={self.title}, status={self.status.value})>"
    
    @property
    def url(self):
        """Return the main photo URL"""
        # This would be implemented based on your S3 setup
        return f"https://your-bucket.s3.amazonaws.com/{self.file_path}"
    
    def get_thumbnail(self, size: int):
        """Get thumbnail URL for specific size"""
        if self.thumbnails and str(size) in self.thumbnails:
            return self.thumbnails[str(size)]
        return self.url  # Fallback to original
