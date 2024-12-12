import os
from pathlib import Path
from dotenv import load_dotenv


if not os.getenv("MODE"):
    load_dotenv(f"{Path(os.path.dirname(os.path.abspath(__file__))).parent.parent}/.dev.env", override=True)


class DBConfig:
    @classmethod
    def DB_NAME(cls) -> str:
        return os.getenv("DATABASE_NAME")
    
    
    @classmethod
    def DB_PASSWORD(cls) -> str:
        return os.getenv("DATABASE_PASSWORD")
    

    @classmethod
    def USER(cls) -> str:
        return os.getenv("USER")


    @classmethod
    def DB_HOST(cls) -> str:
        return os.getenv("HOST")
    

    @classmethod
    def DB_PORT(cls) -> str:
        return os.getenv("PORT")
    

    @classmethod
    def DB_URL(cls) -> str:
        return "postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}".format(
            cls.USER(), 
            cls.DB_PASSWORD(), 
            cls.DB_HOST(), 
            cls.DB_PORT(), 
            cls.DB_NAME()
        )


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
   