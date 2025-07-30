from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.sql import func
from app.database import Base

# Association table for Photo-Tag many-to-many relationship
photo_tags = Table(
    'photo_tags',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('photo_id', Integer, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), nullable=False),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    UniqueConstraint('photo_id', 'tag_id', name='uq_photo_tag')
)

# Association table for Album-Photo many-to-many relationship
album_photos = Table(
    'album_photos',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('album_id', Integer, ForeignKey('albums.id', ondelete='CASCADE'), nullable=False),
    Column('photo_id', Integer, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False),
    Column('sort_order', Integer, default=0),
    Column('created_at', DateTime(timezone=True), server_default=func.now()),
    UniqueConstraint('album_id', 'photo_id', name='uq_album_photo')
)
