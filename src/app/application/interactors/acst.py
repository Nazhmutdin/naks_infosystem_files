from pathlib import Path

from fastapi import UploadFile

from app.application.interfaces.gateways import IAcstFilesGateway
from app.application.dto import CreateAcstFilesDTO
from app.application.common.exc import FileNotFound
from app.utils.path_utils import get_acst_path
from app.infrastructure.fs import save_fastapi_upload_binary_file


class DownloadAcstFileInteractor:

    def __init__(self, gateway: IAcstFilesGateway):
        self.gateway = gateway


    async def __call__(self, acst_number: str) -> Path:
        acst = await self.gateway.get_by_acst_number(acst_number)

        if not acst:
            raise FileNotFound(
                mode="acst",
                filename=acst_number
            )
        
        path = get_acst_path(
            filename=acst.ident.hex
        )
        
        return path


class UploadAcstFileInteractor:

    def __init__(self, gateway: IAcstFilesGateway):
        self.gateway = gateway


    async def __call__(
        self, 
        data: CreateAcstFilesDTO,
        file: UploadFile
    ):
        await self.gateway.insert(data)
        
        file_path = get_acst_path(filename=data.ident.hex)

        await save_fastapi_upload_binary_file(
            file_path=file_path,
            file=file
        )
