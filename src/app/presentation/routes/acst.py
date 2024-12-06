from uuid import UUID, uuid4
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response, Query
from fastapi.responses import FileResponse

from app.application.interactors.acst import DownloadAcstFileInteractor, UploadAcstFileInteractor, GetAcstFileDataByNumberInteractor
from app.application.dto import CreateAcstFilesDTO, AcstFilesDTO


acst_files_router = APIRouter(prefix="/acst")


@acst_files_router.get("/{acst_number}/download")
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


@acst_files_router.get("/by-number/{acst_number}")
@inject
async def get_file_data_by_number(
    acst_number: str,
    get: FromDishka[GetAcstFileDataByNumberInteractor]
) -> AcstFilesDTO:
    return await get(
        acst_number=acst_number
    )


@acst_files_router.post("/")
@inject
async def upload(
    ident: Annotated[UUID, Query(default_factory=uuid4)],
    acst_number: Annotated[str, Query()],
    upload_file: FromDishka[UploadAcstFileInteractor],
    file: UploadFile
) -> Response:
    
    data = CreateAcstFilesDTO(
        ident=ident,
        acst_number=acst_number
    )
    
    await upload_file(data, file)

    return Response(
        "file successfully uploaded"
    )
