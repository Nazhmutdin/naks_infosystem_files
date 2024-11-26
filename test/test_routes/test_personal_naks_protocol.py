from uuid import uuid4

from base_test_routes import BaseTestRoutes

from app.config import AppConfig
from app.application.dto import CreatePersonalNaksProtocolFilesDTO


class TestPersonalNaksProtocolRoutes(BaseTestRoutes):
    _base_endpoint_path = "/personal-naks-protocol"
    _static_subfold_path = AppConfig.personal_naks_protocol_folder()


    def test_upload(self):

        dto = CreatePersonalNaksProtocolFilesDTO(
            ident=uuid4(),
            protocol_number="some_test_number"
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