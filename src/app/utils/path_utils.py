from pathlib import Path

from app.config import AppConfig


def get_acst_path(filename: str) -> Path:
    acst_folder = AppConfig.acst_folder()

    if filename.endswith(".pdf"):
        return acst_folder / filename

    return acst_folder / f"{filename}.pdf"


def get_personal_naks_certification_path(filename: str) -> Path:
    certifiation_folder = AppConfig.personal_naks_certification_folder()

    if filename.endswith(".pdf"):
        return certifiation_folder / filename

    return certifiation_folder / f"{filename}.pdf"


def get_personal_naks_protocol_path(filename: str) -> Path:
    protocol_folder = AppConfig.personal_naks_protocol_folder()

    if filename.endswith(".pdf"):
        return protocol_folder / filename

    return protocol_folder / f"{filename}.pdf"
