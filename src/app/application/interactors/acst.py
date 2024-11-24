from pathlib import Path

from fastapi import UploadFile

from app.application.common.exc import FileNotFound
from app.utils.path_utils import get_acst_path
from app.infrastructure.fs import save_fastapi_upload_binary_file


class DownloadAcstFileInteractor:

    async def __call__(self, filename: str) -> Path:
        path = get_acst_path(
            filename=filename
        )

        if not path.exists():
            raise FileNotFound(
                mode="acst",
                filename=filename
            )
        
        return path


class UploadAcstFileInteractor:

    async def __call__(
        self, 
        filename: str,
        file: UploadFile
    ):
        file_path = get_acst_path(filename=filename)

        await save_fastapi_upload_binary_file(
            file_path=file_path,
            file=file
        )
