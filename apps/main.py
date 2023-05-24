import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.api.routes.users import router as users_router
from apps.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router, prefix="/api")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
