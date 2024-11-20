from base_test_routes import BaseTestRoutes

from app.config import AppConfig


class TestAcstRoutes(BaseTestRoutes):
    _base_endpoint_path = "/personal-naks-certification"
    _static_subfold_path = AppConfig.personal_naks_certification_folder()


    def test_upload(self):

        super().test_upload(
            file_path=AppConfig.static_folder().parent / "base_file.pdf",
            file_name="test_name.pdf"
        )
    

    def test_download(self): 

        super().test_download(
            file_name="base_file.pdf"
        )


    def test_not_found_file(self):
        super().test_not_found_file(
            file_name="not_existing_file_name.pdf"
        )