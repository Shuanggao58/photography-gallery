# Import all models for easy access and to ensure they're registered with SQLAlchemy
from .base import BaseModel
from .user import User
from .category import Category
from .tag import Tag
from .photo import Photo, PhotoStatus
from .album import Album, AlbumVisibility
from .associations import photo_tags, album_photos

# Export all models
__all__ = [
    "BaseModel",
    "User", 
    "Category",
    "Tag",
    "Photo",
    "PhotoStatus",
    "Album", 
    "AlbumVisibility",
    "photo_tags",
    "album_photos"
]
