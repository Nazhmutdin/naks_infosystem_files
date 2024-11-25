from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_certification import (
    DownloadPersonalNaksCertificationFileInteractor, 
    UploadPersonalNaksCertificationFileInteractor
)


personal_naks_certification_files_router = APIRouter(prefix="/personal-naks-certification")


@personal_naks_certification_files_router.get("/download/{certification_number}")
@inject
async def download(
    certification_number: str,
    get_path: FromDishka[DownloadPersonalNaksCertificationFileInteractor]
) -> FileResponse:
    path = await get_path(certification_number)

    return FileResponse(
        path=path,
        filename=path.name,
        media_type="application/pdf"
    )


@personal_naks_certification_files_router.post("/upload/{certification_number}")
@inject
async def upload(
    certification_number: str,
    upload_file: FromDishka[UploadPersonalNaksCertificationFileInteractor],
    file: UploadFile
) -> Response:
    await upload_file(certification_number, file)

    return Response(
        "file successfully uploaded"
    )
