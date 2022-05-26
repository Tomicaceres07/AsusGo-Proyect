from pydantic import BaseModel
from typing import Optional

class Request(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None
    mail: Optional[str] = None
    type: Optional[str] = None
    code: Optional[str] = None