from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.db.session import get_db

from app.api.v1.auth import router as auth_router
from app.api.v1.employees import router as employees_router   # ← ADD THIS
from app.api.v1.departments import router as departments_router
from app.api.v1.leaves import router as leave_router
from app.api.v1.leave_balance import router as leave_balance_router
from app.api.v1.attendance import router as attendance_router
from app.api.v1.onboarding import router as onboarding_router
from app.api.v1.payroll import router as payroll_router
from app.api.v1.performance import router as performance_router
from app.api.v1.reports import router as reports_router
from app.api.v1.ai import router as ai_router



app = FastAPI(
    title="University HRM System API",
    description="Backend for University HRM",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "University HRM System Backend is LIVE! 🚀 Welcome Divyansh!"}

@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

# Mount all routers
app.include_router(auth_router, prefix="/api/v1")
app.include_router(departments_router, prefix="/api/v1")
app.include_router(leave_router, prefix="/api/v1")
app.include_router(leave_balance_router, prefix="/api/v1")
app.include_router(attendance_router, prefix="/api/v1")
app.include_router(onboarding_router, prefix="/api/v1")
app.include_router(payroll_router, prefix="/api/v1")
app.include_router(performance_router, prefix="/api/v1")
app.include_router(reports_router,     prefix="/api/v1")
app.include_router(ai_router, prefix="/api/v1")
