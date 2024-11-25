from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_protocol import (
    DownloadPersonalNaksProtocolFileInteractor, 
    UploadPersonalNaksProtocolFileInteractor
)


personal_naks_protocol_files_router = APIRouter(prefix="/personal-naks-protocol")


@personal_naks_protocol_files_router.get("/download/{protocol_number}")
@inject
async def download(
    protocol_number: str,
    get_path: FromDishka[DownloadPersonalNaksProtocolFileInteractor]
) -> FileResponse:
    
    path = await get_path(protocol_number)

    return FileResponse(
        path=path,
        filename=path.name,
        media_type="application/pdf"
    )


@personal_naks_protocol_files_router.post("/upload/{protocol_number}")
@inject
async def upload(
    protocol_number: str,
    upload_file: FromDishka[UploadPersonalNaksProtocolFileInteractor],
    file: UploadFile
) -> Response:
    await upload_file(protocol_number, file)

    return Response(
        "file successfully uploaded"
    )
