from fastapi import Request
from fastapi.responses import ORJSONResponse

from app.application.common.exc import FileNotFound


async def file_not_found_exception_handler(
    request: Request,
    exception: FileNotFound
):
    return ORJSONResponse(
        status_code=404,
        content={
            "code": f"{exception.mode}_file_not_found",
            "detail": f"{exception.mode.replace("_", " ")} ({exception.filename}) not found"
        }
    )
