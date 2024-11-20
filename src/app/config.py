import os
from pathlib import Path
from dotenv import load_dotenv


if not os.getenv("MODE"):
    load_dotenv(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent.parent}/.dev.env")


class AppConfig:

    @classmethod
    def cwd(cls) -> Path:
        return Path.cwd()
    

    @classmethod
    def static_folder(cls) -> Path:
        return Path(os.getenv("STATIC_PATH"))
    
    
    @classmethod
    def acst_folder(cls) -> Path:
        return cls.static_folder() / "acst"
    

    @classmethod
    def personal_naks_certification_folder(cls) -> Path:
        return cls.static_folder() / "personal_naks_certification"
    

    @classmethod
    def personal_naks_protocol_folder(cls) -> Path:
        return cls.static_folder() / "personal_naks_protocol"
    