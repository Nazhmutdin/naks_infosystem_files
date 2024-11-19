from pathlib import Path


class AppConfig:

    @classmethod
    def cwd(cls) -> Path:
        return Path.cwd()
    
    
    @classmethod
    def acst_folder(cls) -> Path:
        return cls.cwd().parent / "static" / "acst"
    

    @classmethod
    def personal_naks_certification_folder(cls) -> Path:
        return cls.cwd().parent / "static" / "personal_naks_certification"
    