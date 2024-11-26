from uuid import uuid4

from base_test_routes import BaseTestRoutes

from app.config import AppConfig
from app.application.dto import CreateAcstFilesDTO


class TestAcstRoutes(BaseTestRoutes):
    _base_endpoint_path = "/acst"
    _static_subfold_path = AppConfig.acst_folder()


    def test_upload(self):

        dto = CreateAcstFilesDTO(
            ident=uuid4(),
            acst_number="some_test_number"
        )

        super().test_upload(
            file_path=AppConfig.static_folder().parent / "base_file.pdf",
            data=dto
        )
    

    def test_download(self): 

        super().test_download(
            number="test_number"
        )


    def test_not_found_file(self):
        super().test_not_found_file(
            number="not_existing_number"
        )