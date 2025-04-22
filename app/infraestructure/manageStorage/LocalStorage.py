from http.client import HTTPException

from fastapi import UploadFile
import shutil
import os

from app.infraestructure.manageStorage.StorageInterface import StorageInterface

class LocalStorage(StorageInterface):

    def __init__(self, base_path: str = "../files"):
        self.base_path = os.path.abspath(base_path)
        os.makedirs(self.base_path, exist_ok=True)

    async def save(self, file: UploadFile, filename: str) -> dict[str, str]:
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"path":file_path, "filename":filename}

    async def get_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.isfile(file_path):
            raise HTTPException(status_code=404, detail="Archivo no encontrado")
        return file_path
