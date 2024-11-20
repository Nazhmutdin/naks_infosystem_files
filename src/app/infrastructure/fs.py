from pathlib import Path

from aiofiles import open
from fastapi import UploadFile


CHUNCK_SIZE = 1024 * 1024


async def save_fastapi_upload_binary_file(
    file_path: Path,
    file: UploadFile
):
    chunck_amount = file.size / CHUNCK_SIZE

    async with open(file_path, "wb") as f:

        for _ in range(int(chunck_amount) + 1):
            chunck = await file.read(CHUNCK_SIZE)
            await f.write(chunck)

        await f.close()
