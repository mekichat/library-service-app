from app.bootstrap import *

# Create FastAPI App
from fastapi import FastAPI

from app.database import Base, engine
from app import models   # IMPORTANT (forces table registration)
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


import time
from pathlib import Path
from sqlalchemy.exc import OperationalError



app = FastAPI(
        
    docs_url="/docs",
    openapi_url="/openapi.json",
    title="📚 Book Service API",
    description="""
    A production-grade microservice for managing books in a distributed library system.
    
    ## Services
    - 📘 Book Service (FastAPI + MySQL)
    - 📦 Order Service (Go + PostgreSQL)

    Features:
    - Clean REST architecture
    - Create, Read, Update, Delete books
    - MySQL persistence using SQLAlchemy
    - Designed for microservice architecture (Book + Order services)
    - Swagger-based testing
    - Docker & Kubernetes ready
    """,
    version="1.0.0",
    contact={
        "name": "Library System Team",
        "email": "mekuriategegne@gmail.com"
    },
    license_info={
        "name": "YH Akademin License"
    },
    swagger_ui_parameters={
        "docExpansion": "none",
        "defaultModelsExpandDepth": -1,
        "displayRequestDuration": True,
        "filter": True,
        "tryItOutEnabled": True
    }
)

STATIC_DIR = Path(__file__).parent / "static"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

for i in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        print("DB connected + tables created")
        break
    except Exception as e:
        print("REAL ERROR:", repr(e))
        time.sleep(3)
        

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

from fastapi.openapi.docs import get_swagger_ui_html

@app.get("/docs", include_in_schema=False)
def swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Book Service API",
        swagger_favicon_url="/static/favicon.png",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger.css"
    )