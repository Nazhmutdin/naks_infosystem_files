import hashlib
import os
from pathlib import Path

from client import client


class BaseTestRoutes:
    _base_endpoint_path: str
    _static_subfold_path: Path


    def test_upload(self, file_path: Path, file_name: str):
        before_files_amount = len(os.listdir(self._static_subfold_path))

        file = open(file_path, "rb")

        res = client.post(
            f"{self._base_endpoint_path}/upload/{file_name}",
            files={
                "file": file
            }
        )

        file.close()
        
        after_files_amount = len(os.listdir(self._static_subfold_path))

        assert res.status_code == 200
        assert (after_files_amount - before_files_amount) == 1

        os.remove(self._static_subfold_path / file_name)


    def test_download(self, file_name: str):
        res = client.post(
            f"{self._base_endpoint_path}/download/{file_name}"
        )

        res_checksum = self.compute_checksum(res.content)
        file_checksum = self.compute_checksum(open(self._static_subfold_path.parent.parent / "base_file.pdf", "rb").read())

        assert res_checksum == file_checksum
        assert res.status_code == 200


    def test_not_found_file(self, file_name: str):
        res = client.post(
            f"{self._base_endpoint_path}/download/{file_name}"
        )
        
        assert res.status_code == 404


    def compute_checksum(self, data: str | bytes) -> str:
        return hashlib.md5(data).hexdigest()
