from uuid import UUID, uuid4
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response, Query
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_protocol import (
    DownloadPersonalNaksProtocolFileInteractor, 
    UploadPersonalNaksProtocolFileInteractor,
    GetPersonalNaksProtocolFileDataByNumberInteractor
)
from app.application.dto import CreatePersonalNaksProtocolFilesDTO, PersonalNaksProtocolFilesDTO


personal_naks_protocol_files_router = APIRouter(prefix="/personal-naks-protocol")


@personal_naks_protocol_files_router.get("/{protocol_number}/download")
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


@personal_naks_protocol_files_router.get("/by-number/{protocol_number}")
@inject
async def get_file_data_by_number(
    protocol_number: str,
    get: FromDishka[GetPersonalNaksProtocolFileDataByNumberInteractor]
) -> PersonalNaksProtocolFilesDTO:
    return await get(
        protocol_number=protocol_number
    )


@personal_naks_protocol_files_router.post("/")
@inject
async def upload(
    ident: Annotated[UUID, Query(default_factory=uuid4)],
    protocol_number: Annotated[str, Query()],
    upload_file: FromDishka[UploadPersonalNaksProtocolFileInteractor],
    file: UploadFile
) -> Response:
    
    data = CreatePersonalNaksProtocolFilesDTO(
        ident=ident,
        protocol_number=protocol_number
    )
    await upload_file(data, file)

    return Response(
        "file successfully uploaded"
    )
