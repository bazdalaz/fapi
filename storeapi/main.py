from fastapi import FastAPI
from storeapi.routers import router as post_router

app = FastAPI()

app.include_router(post_router)