# Photography Gallery

A modern, responsive photography gallery website showcasing professional photography work.

## Tech Stack

**Frontend:**
- Next.js 14+ with App Router
- TypeScript
- Tailwind CSS
- Radix UI
- React Query

**Backend:**
- FastAPI (Python)
- SQLAlchemy + Alembic
- PostgreSQL
- AWS S3 for image storage

**Infrastructure:**
- AWS (EC2, RDS, S3, CloudFront)
- Terraform
- GitHub Actions CI/CD

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL
- AWS CLI
- Terraform

### Local Development

1. Clone the repository
```bash
git clone https://github.com/Shuanggao58/photography-gallery.git
cd photography-gallery
```

2. Set up the frontend
```bash
cd frontend
npm install
npm run dev
```

3. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

4. Set up the database
```bash
# Run migrations
alembic upgrade head
```

## Project Structure

- `frontend/` - Next.js application
- `backend/` - FastAPI application
- `infrastructure/` - Terraform configurations
- `docs/` - Project documentation
- `.github/workflows/` - CI/CD pipelines

## Development Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run tests locally
4. Create a pull request
5. Deploy after review and merge

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details
