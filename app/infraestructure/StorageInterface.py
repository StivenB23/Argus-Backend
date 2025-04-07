from abc import ABC, abstractmethod
from fastapi import UploadFile


class StorageInterface(ABC):

    @abstractmethod
    async def save(self, file: UploadFile, filename: str) -> str:
        """Guarda un archivo y retorna la URL o ruta"""
        pass
