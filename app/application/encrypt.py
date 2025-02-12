import bcrypt
from cryptography.fernet import Fernet


def hash_password(plain_text_password: str)->str:
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

def check_password(plain_text_password: str, hashed_password: str) -> bool:
    password_bytes = plain_text_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

    
def encrypt_text(texto_plano: str, clave: bytes | str) -> str:
    fernet = Fernet(clave)
    texto_encriptado = fernet.encrypt(texto_plano.encode('utf-8'))
    return texto_encriptado.decode('utf-8')


def decrypt_text(texto_encriptado: str, clave: bytes |str) -> str:
    fernet = Fernet(clave)
    texto_desencriptado = fernet.decrypt(texto_encriptado.encode('utf-8'))
    return texto_desencriptado.decode('utf-8')