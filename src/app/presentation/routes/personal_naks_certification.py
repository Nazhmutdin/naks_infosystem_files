from uuid import UUID, uuid4
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response, Query
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_certification import (
    DownloadPersonalNaksCertificationFileInteractor, 
    UploadPersonalNaksCertificationFileInteractor
)
from app.application.dto import CreatePersonalNaksCertificationFilesDTO


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


@personal_naks_certification_files_router.post("/upload")
@inject
async def upload(
    ident: Annotated[UUID, Query(default_factory=uuid4)],
    certification_numbers: Annotated[list[str], Query()],
    upload_file: FromDishka[UploadPersonalNaksCertificationFileInteractor],
    file: UploadFile
) -> Response:
    
    data = CreatePersonalNaksCertificationFilesDTO(
        ident=ident,
        certification_numbers=certification_numbers
    )
    await upload_file(data, file)

    return Response(
        "file successfully uploaded"
    )
