from pathlib import Path

from fastapi import UploadFile

from app.application.common.exc import FileNotFound
from app.utils.path_utils import get_personal_naks_certification_path
from app.infrastructure.fs import save_fastapi_upload_binary_file


class DownloadPersonalNaksCertificationFileInteractor:

    async def __call__(self, filename: str) -> Path:
        path = get_personal_naks_certification_path(
            filename=filename
        )

        if not path.exists():
            raise FileNotFound(
                mode="personal_naks_certification",
                filename=filename
            )
        
        return path


class UploadPersonalNaksCertificationFileInteractor:

    async def __call__(
        self, 
        filename: str,
        file: UploadFile
    ):
        file_path = get_personal_naks_certification_path(filename=filename)

        await save_fastapi_upload_binary_file(
            file_path=file_path,
            file=file
        )
