from datetime import datetime
import re

def create_uuid(role, document_number:str)->str:
    now = datetime.now()
    year = now.year
    doc_part = document_number[-4:].zfill(4)
    timestamp = now.strftime("%H%M%S")
    return f"{role}-{year}-{doc_part}-{timestamp}"

def is_valid_uuid_format(uuid_str: str) -> bool:
    pattern = r"^[a-zA-Z0-9]+-\d{4}-\d{4}-\d{6}$"
    return re.match(pattern, uuid_str) is not None
