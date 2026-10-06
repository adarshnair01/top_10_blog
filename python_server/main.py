import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_routes import router

app = FastAPI(
    title="Top 10 AI Story Post Generator API",
    description="Engine for generating fact-checked, story-driven Top 10 countdown blogs on trending topics.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def health_check():
    return {
        "status": "active",
        "service": "Top 10 AI Story Generator Engine",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)
