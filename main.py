from fastapi import FastAPI
from starlette.responses import HTMLResponse
from models import models
from database.configuration import engine
from core import blog, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BlogAPI",
    description="My blog",
    version="1.0.0",)

app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(user.router)

