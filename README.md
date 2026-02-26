# University HRM System - Backend

FastAPI + Async SQLAlchemy + PostgreSQL backend for a modern University Human Resource Management System.

Built with clean architecture, full JWT Authentication + Role-Based Access Control (RBAC), and ready for frontend integration.

---

 🚀 Quick Start 

1. Clone the repository
```bash
git clone https://github.com/Divyansh1132/university-hrm-backend.git
cd university-hrm-backend

2. Backend Setup (Local Development)

Bash# Create virtual environment
uv venv

# Activate
# Windows
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Run the server
uv run uvicorn app.main:app --reload --port 8000

3. First Time Setup (Run Once)
Bash# Seed default data (Admin, HR, Accountant, HOD, Employee + Departments)
uv run python seed.py

4. API Documentation

Interactive Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
OpenAPI JSON: http://localhost:8000/openapi.json

All protected routes require Bearer <token> in Authorization header.

🛠 Tech Stack

Framework: FastAPI (Python 3.13)
Database: PostgreSQL + SQLAlchemy 2.0 (async)
ORM: Async SQLAlchemy
Migrations: Alembic
Auth: JWT + Argon2 password hashing
Role System: Admin, HR, Department Head, Accountant, Employee
Dependency Management: uv / pip

