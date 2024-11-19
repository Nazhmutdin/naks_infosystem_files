from pathlib import Path

from app.config import AppConfig


class DownloadFileInteractor:
    def __init__(self) -> None: ...


    async def __call__(self, acst_number: str) -> Path:
        acst_folder = AppConfig.acst_folder()

        return acst_folder / f"{acst_number}.pdf"
