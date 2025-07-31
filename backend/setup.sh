# Create basic app structure
mkdir -p app/api app/models tests

# Create basic app files
echo 'from fastapi import FastAPI

app = FastAPI(
    title="Photography Gallery API",
    description="A modern photography gallery API",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Photography Gallery API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
' > app/main.py

# Create empty __init__.py files
touch app/__init__.py
touch app/api/__init__.py
touch app/models/__init__.py
touch tests/__init__.py

# Create basic test
echo 'import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Photography Gallery API"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
' > tests/test_main.py

echo "Backend structure created successfully!"
