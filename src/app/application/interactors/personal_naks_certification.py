from pathlib import Path

from fastapi import UploadFile
from naks_library.interfaces import ICommitter

from app.application.interfaces.gateways import IPersonalNaksCertificationFilesGateway
from app.application.dto import CreatePersonalNaksCertificationFilesDTO, PersonalNaksCertificationFilesDTO
from app.application.common.exc import FileNotFound
from app.utils.path_utils import get_personal_naks_certification_path
from app.infrastructure.fs import save_fastapi_upload_binary_file


class DownloadPersonalNaksCertificationFileInteractor:

    def __init__(self, gateway: IPersonalNaksCertificationFilesGateway):
        self.gateway = gateway


    async def __call__(self, certification_number: str) -> Path:
        cert = await self.gateway.get_by_certification_number(certification_number)

        if not cert:
            raise FileNotFound(
                mode="personal_naks_certification",
                filename=certification_number
            )

        path = get_personal_naks_certification_path(
            filename=cert.ident.hex
        )
        
        return path


class UploadPersonalNaksCertificationFileInteractor:

    def __init__(
        self, 
        gateway: IPersonalNaksCertificationFilesGateway,
        committer: ICommitter
    ):
        self.gateway = gateway
        self.committer = committer


    async def __call__(
        self, 
        data: CreatePersonalNaksCertificationFilesDTO,
        file: UploadFile
    ):
        await self.gateway.insert(data)

        await self.committer.commit()

        file_path = get_personal_naks_certification_path(filename=data.ident.hex)

        await save_fastapi_upload_binary_file(
            file_path=file_path,
            file=file
        )


class GetPersonalNaksCertificationFileDataByNumberInteractor:

    def __init__(self, gateway: IPersonalNaksCertificationFilesGateway):
        self.gateway = gateway

    
    async def __call__(self, certification_number: str) -> PersonalNaksCertificationFilesDTO:
        res = await self.gateway.get_by_certification_number(certification_number=certification_number)

        if not res:
            raise FileNotFound(
                mode="personal_naks_certification",
                filename=certification_number
            )
        
        return res
