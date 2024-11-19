from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from app.main.dependencies import AppProvider
from app.presentation.routes.acst import acst_files_router


app = FastAPI()
container = make_async_container(AppProvider())

setup_dishka(container=container, app=app)


app.include_router(acst_files_router)
