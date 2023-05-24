import uvicorn
from fastapi import FastAPI
from apps.api.routes.users import router as users_router
from apps.db.session import Base, engine

# Create an instance of the FastAPI app
app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(users_router, prefix="/api")

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
