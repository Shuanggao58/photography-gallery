# Development Setup Guide

This guide will help you set up the Photography Gallery project for local development.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (version 18 or higher)
- **Python** (version 3.11 or higher)
- **PostgreSQL** (version 13 or higher)
- **Git**

## Quick Start with Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Shuanggao58/photography-gallery.git
cd photography-gallery
```

2. Start all services with Docker Compose:
```bash
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- Redis on port 6379
- Backend API on port 8000
- Frontend app on port 3000

## Manual Setup

### 1. Database Setup

Create a PostgreSQL database:
```sql
CREATE DATABASE photography_gallery;
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your database credentials

# Run database migrations
alembic upgrade head

# Start the development server
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.local.example .env.local
# Edit .env.local with your API URL

# Start the development server
npm run dev
```

The frontend will be available at http://localhost:3000

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://username:password@localhost:5432/photography_gallery
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-here
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-s3-bucket-name
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Useful Commands

### Backend
- `uvicorn app.main:app --reload` - Start development server
- `alembic revision --autogenerate -m "description"` - Create migration
- `alembic upgrade head` - Apply migrations
- `pytest` - Run tests

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript checks

## Project Structure

```
photography-gallery/
├── frontend/          # Next.js application
│   ├── src/
│   │   ├── app/       # App router pages
│   │   ├── components/ # Reusable components
│   │   ├── lib/       # Utility functions
│   │   └── types/     # TypeScript types
│   └── public/        # Static assets
├── backend/           # FastAPI application
│   ├── app/
│   │   ├── api/       # API routes
│   │   ├── models/    # Database models
│   │   ├── services/  # Business logic
│   │   └── utils/     # Utility functions
│   └── tests/         # Test files
├── infrastructure/    # Terraform configurations
└── docs/             # Documentation
```

## Next Steps

1. Set up your AWS S3 bucket for image storage
2. Configure your environment variables
3. Start developing new features
4. Check the project tasks in your Apple Notes for the development roadmap

## Troubleshooting

### Common Issues

1. **Database connection errors**: Ensure PostgreSQL is running and credentials are correct
2. **Port already in use**: Kill processes on ports 3000, 8000, or 5432
3. **Permission errors**: Ensure proper file permissions and virtual environment activation

### Getting Help

- Check the API documentation at http://localhost:8000/docs
- Review the GitHub Issues for known problems
- Consult the project documentation in the `docs/` folder
