from fastapi import UploadFile
import shutil
import os

from app.infraestructure.StorageInterface import StorageInterface

class LocalStorage(StorageInterface):

    def __init__(self, base_path: str = "../files"):
        self.base_path = os.path.abspath(base_path)
        os.makedirs(self.base_path, exist_ok=True)

    async def save(self, file: UploadFile, filename: str) -> str:
        print("archivo")
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return file_path