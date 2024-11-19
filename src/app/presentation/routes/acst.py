from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.application.interactors.acst import DownloadFileInteractor


acst_files_router = APIRouter(prefix="/acst")


@acst_files_router.post("/download/{acst_number}")
@inject
async def download(
    acst_number: str,
    get_path: FromDishka[DownloadFileInteractor]
) -> FileResponse:
    path = await get_path(acst_number)

    return FileResponse(
        path=path,
        filename=path.name,
        media_type="application/pdf"
    )
