# Database Models Documentation

## Overview

The Photography Gallery uses a comprehensive database schema designed to handle photos, albums, categories, tags, and user management. The models are built using SQLAlchemy ORM with PostgreSQL as the database backend.

## Database Schema

### Core Models

#### User Model
- **Purpose**: Authentication and photo ownership
- **Key Fields**: username, email, hashed_password, is_active, is_superuser
- **Relationships**: Owns photos and albums

#### Photo Model (Main Entity)
- **Purpose**: Core photo entity with metadata and file information
- **Key Fields**: 
  - Basic: title, slug, description, alt_text
  - File: original_filename, file_path, file_size, mime_type
  - Image: width, height, aspect_ratio
  - EXIF: camera_make, camera_model, lens, aperture, etc.
  - Location: location_name, latitude, longitude
  - Stats: view_count, download_count, like_count
- **Status Enum**: UPLOADING, PROCESSING, PUBLISHED, DRAFT, ARCHIVED
- **Relationships**: Belongs to user and category, has many tags and albums

#### Album Model
- **Purpose**: Photo collections/galleries
- **Key Fields**: title, slug, description, visibility, photo_count
- **Visibility Enum**: PUBLIC, PRIVATE, UNLISTED
- **Relationships**: Belongs to user, contains many photos

#### Category Model
- **Purpose**: Photo categorization (Portrait, Landscape, Wedding, etc.)
- **Key Fields**: name, slug, description, color, icon
- **Relationships**: Has many photos

#### Tag Model
- **Purpose**: Flexible photo tagging system
- **Key Fields**: name, slug, description, color, usage_count
- **Relationships**: Many-to-many with photos

### Association Tables

#### photo_tags
- Links photos to tags (many-to-many)
- Fields: photo_id, tag_id, created_at

#### album_photos
- Links albums to photos (many-to-many)
- Fields: album_id, photo_id, sort_order, created_at

## Key Features

### 1. UUID Support
- All models have UUID fields for public identification
- Prevents enumeration attacks and provides clean URLs

### 2. Soft Deletes Ready
- Timestamp fields (created_at, updated_at) on all models
- Ready for soft delete implementation if needed

### 3. SEO Optimization
- Slug fields for SEO-friendly URLs
- Meta title and description fields
- Alt text for accessibility

### 4. Image Management
- Multiple thumbnail sizes stored as JSON
- EXIF data preservation
- File size and dimension tracking
- Status-based processing workflow

### 5. Performance Optimizations
- Indexed fields for common queries
- Cached counters (photo_count, usage_count)
- Efficient many-to-many relationships

## Database Setup Commands

### 1. Initialize Alembic (First Time Only)
```bash
cd backend
alembic init alembic  # Already done in the repo
```

### 2. Create Initial Migration
```bash
cd backend
alembic revision --autogenerate -m "Initial migration with all models"
```

### 3. Apply Migrations
```bash
cd backend
alembic upgrade head
```

### 4. Create New Migration After Model Changes
```bash
cd backend
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Usage Examples

### 1. Create a User
```python
from app.models import User
from app.database import SessionLocal

db = SessionLocal()
user = User(
    username="photographer",
    email="photographer@example.com",
    hashed_password="hashed_password_here",
    full_name="John Photographer"
)
db.add(user)
db.commit()
```

### 2. Create a Photo with Tags
```python
from app.models import Photo, Tag, PhotoStatus

# Create photo
photo = Photo(
    title="Beautiful Sunset",
    slug="beautiful-sunset",
    description="A stunning sunset over the ocean",
    original_filename="sunset.jpg",
    file_path="photos/2024/sunset.jpg",
    file_size=2048000,
    mime_type="image/jpeg",
    width=1920,
    height=1080,
    status=PhotoStatus.PUBLISHED,
    owner_id=user.id
)

# Create/get tags
nature_tag = Tag(name="nature", slug="nature")
sunset_tag = Tag(name="sunset", slug="sunset")

# Add tags to photo
photo.tags.extend([nature_tag, sunset_tag])

db.add(photo)
db.commit()
```

### 3. Create an Album
```python
from app.models import Album, AlbumVisibility

album = Album(
    title="Nature Photography",
    slug="nature-photography",
    description="Collection of nature photos",
    visibility=AlbumVisibility.PUBLIC,
    owner_id=user.id
)

# Add photos to album
album.photos.append(photo)

db.add(album)
db.commit()
```

## Migration Strategy

### Development
1. Make model changes
2. Generate migration: `alembic revision --autogenerate -m "description"`
3. Review generated migration file
4. Apply migration: `alembic upgrade head`

### Production
1. Test migrations on staging environment
2. Backup production database
3. Apply migrations: `alembic upgrade head`
4. Verify data integrity

## Indexes and Performance

### Recommended Indexes (automatically created by SQLAlchemy)
- Users: username, email
- Photos: slug, status, owner_id, category_id
- Albums: slug, visibility, owner_id
- Categories: slug, name
- Tags: slug, name

### Performance Considerations
- Use pagination for photo listings
- Implement caching for category/tag counts
- Consider database connection pooling for high traffic
- Monitor query performance with database logs

## Backup and Recovery

### Regular Backups
```bash
# Database backup
pg_dump photography_gallery > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore from backup
psql photography_gallery < backup_file.sql
```

### Migration Rollbacks
```bash
# Rollback one migration
alembic downgrade -1

# Rollback to specific revision
alembic downgrade <revision_id>
```
