from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from app.main.dependencies import AppProvider

from app.application.common.exc import FileNotFound

from app.presentation.routes.acst import acst_files_router
from app.presentation.routes.personal_naks_certification import personal_naks_certification_files_router
from app.presentation.routes.personal_naks_protocol import personal_naks_protocol_files_router
from app.presentation.routes.exc_handlers import file_not_found_exception_handler


app = FastAPI()
container = make_async_container(AppProvider())

setup_dishka(container=container, app=app)


app.include_router(acst_files_router)
app.include_router(personal_naks_certification_files_router)
app.include_router(personal_naks_protocol_files_router)

app.add_exception_handler(
    FileNotFound,
    file_not_found_exception_handler
)
