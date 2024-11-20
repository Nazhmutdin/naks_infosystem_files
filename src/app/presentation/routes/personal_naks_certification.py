from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_certification import (
    DownloadPersonalNaksCertificationFileInteractor, 
    UploadPersonalNaksCertificationFileInteractor
)


personal_naks_certification_files_router = APIRouter(prefix="/personal-naks-certification")


@personal_naks_certification_files_router.post("/download/{filename}")
@inject
async def download(
    filename: str,
    get_path: FromDishka[DownloadPersonalNaksCertificationFileInteractor]
) -> FileResponse:
    path = await get_path(filename)

    return FileResponse(
        path=path,
        filename=path.name,
        media_type="application/pdf"
    )


@personal_naks_certification_files_router.post("/upload/{filename}")
@inject
async def upload(
    filename: str,
    upload_file: FromDishka[UploadPersonalNaksCertificationFileInteractor],
    file: UploadFile
) -> Response:
    await upload_file(filename, file)

    return Response(
        "file successfully uploaded"
    )
