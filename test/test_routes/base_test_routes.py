import hashlib
import os
from pathlib import Path
from uuid import UUID

import pytest

from client import client


class ICreateDTO:
    ident: UUID


@pytest.mark.usefixtures("add_default_values")
class BaseTestRoutes:
    _base_endpoint_path: str
    _static_subfold_path: Path


    def test_upload(self, file_path: Path, number: str):
        before_files_amount = len(os.listdir(self._static_subfold_path))

        file = open(file_path, "rb")

        res = client.post(
            f"{self._base_endpoint_path}/by-number/{number}/upload",
            files={
                "file": file
            }
        )

        file.close()
        
        after_files_amount = len(os.listdir(self._static_subfold_path))

        assert res.status_code == 200
        assert (after_files_amount - before_files_amount) == 1

        for file in os.listdir(self._static_subfold_path):
            if file == "f6500b2b9a054e5a852fbb7b88efee8b.pdf":
                continue
            
            os.remove(self._static_subfold_path / file)


    def test_download(self, number: str):
        res = client.get(
            f"{self._base_endpoint_path}/by-number/{number}/download"
        )

        res_checksum = self.compute_checksum(res.content)
        file_checksum = self.compute_checksum(open(self._static_subfold_path.parent.parent / "base_file.pdf", "rb").read())

        assert res_checksum == file_checksum
        assert res.status_code == 200


    def test_not_found_file(self, number: str):
        res = client.get(
            f"{self._base_endpoint_path}/by-number/{number}"
        )
        
        assert res.status_code == 404


    def test_get_file_data(self, number: str):
        res = client.get(
            f"{self._base_endpoint_path}/by-number/{number}"
        )
        
        assert res.status_code == 200


    def compute_checksum(self, data: str | bytes) -> str:
        return hashlib.md5(data).hexdigest()
