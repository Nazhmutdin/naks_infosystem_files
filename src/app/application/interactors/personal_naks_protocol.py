from pathlib import Path

from fastapi import UploadFile
from naks_library.interfaces import ICommitter

from app.application.interfaces.gateways import IPersonalNaksProtocolFilesGateway
from app.application.dto import CreatePersonalNaksCertificationFilesDTO, PersonalNaksProtocolFilesDTO
from app.application.common.exc import FileNotFound
from app.utils.path_utils import get_personal_naks_protocol_path
from app.infrastructure.fs import save_fastapi_upload_binary_file


class DownloadPersonalNaksProtocolFileInteractor:

    def __init__(self, gateway: IPersonalNaksProtocolFilesGateway):
        self.gateway = gateway


    async def __call__(self, protocol_number: str) -> Path:
        prot = await self.gateway.get_by_protocol_number(protocol_number)

        if not prot:
            raise FileNotFound(
                mode="personal_naks_protocol",
                filename=protocol_number
            )

        path = get_personal_naks_protocol_path(
            filename=prot.ident.hex
        )
        
        return path


class UploadPersonalNaksProtocolFileInteractor:

    def __init__(
        self, 
        gateway: IPersonalNaksProtocolFilesGateway,
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

        file_path = get_personal_naks_protocol_path(filename=data.ident.hex)

        await save_fastapi_upload_binary_file(
            file_path=file_path,
            file=file
        )


class GetPersonalNaksProtocolFileDataByNumberInteractor:

    def __init__(self, gateway: IPersonalNaksProtocolFilesGateway):
        self.gateway = gateway

    
    async def __call__(self, protocol_number: str) -> PersonalNaksProtocolFilesDTO:
        res = await self.gateway.get_by_protocol_number(protocol_number=protocol_number)

        if not res:
            raise FileNotFound(
                mode="personal_naks_protocol",
                filename=protocol_number
            )
        
        return res
