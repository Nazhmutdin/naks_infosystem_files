from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response
from fastapi.responses import FileResponse

from app.application.interactors.acst import DownloadAcstFileInteractor, UploadAcstFileInteractor


acst_files_router = APIRouter(prefix="/acst")


@acst_files_router.get("/download/{acst_number}")
@inject
async def download(
    acst_number: str,
    get_path: FromDishka[DownloadAcstFileInteractor]
) -> FileResponse:
    path = await get_path(acst_number)

    return FileResponse(
        path=path,
        filename=path.name,
        media_type="application/pdf"
    )


@acst_files_router.post("/upload/{acst_number}")
@inject
async def upload(
    acst_number: str,
    upload_file: FromDishka[UploadAcstFileInteractor],
    file: UploadFile
) -> Response:
    await upload_file(acst_number, file)

    return Response(
        "file successfully uploaded"
    )
