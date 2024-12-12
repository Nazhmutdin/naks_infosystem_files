from base_test_routes import BaseTestRoutes

from app.config import AppConfig


class TestAcstRoutes(BaseTestRoutes):
    _base_endpoint_path = "/acst"
    _static_subfold_path = AppConfig.acst_folder()


    def test_upload(self):

        super().test_upload(
            file_path=AppConfig.static_folder().parent / "base_file.pdf",
            number="some_test_number"
        )
    

    def test_download(self): 

        super().test_download(
            number="test_number"
        )


    def test_not_found_file(self):
        super().test_not_found_file(
            number="not_existing_number"
        )

    
    def test_get_file_data(self):
        super().test_get_file_data("some_test_number")
