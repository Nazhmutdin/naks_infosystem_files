from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, UploadFile, Response
from fastapi.responses import FileResponse

from app.application.interactors.personal_naks_certification import (
    DownloadPersonalNaksCertificationFileInteractor, 
    UploadPersonalNaksCertificationFileInteractor,
    GetPersonalNaksCertificationFileDataByNumberInteractor
)
from app.application.dto import CreatePersonalNaksCertificationFilesDTO, PersonalNaksCertificationFilesDTO


personal_naks_certification_files_router = APIRouter(prefix="/personal-naks-certification")


@personal_naks_certification_files_router.get("/by-number/{certification_number}/download")
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


@personal_naks_certification_files_router.get("/by-number/{certification_number}")
@inject
async def get_file_data_by_number(
    certification_number: str,
    get: FromDishka[GetPersonalNaksCertificationFileDataByNumberInteractor]
) -> PersonalNaksCertificationFilesDTO:
    return await get(
        certification_number=certification_number
    )


@personal_naks_certification_files_router.post("/by-number/{certification_number}/upload")
@inject
async def upload(
    certification_number: str,
    upload_file: FromDishka[UploadPersonalNaksCertificationFileInteractor],
    file: UploadFile
) -> Response:
    
    data = CreatePersonalNaksCertificationFilesDTO(
        certification_number=certification_number
    )
    await upload_file(data, file)

    return Response(
        "file successfully uploaded"
    )
