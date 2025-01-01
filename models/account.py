from pydantic import BaseModel, EmailStr
from uuid import uuid4

class Account(BaseModel):
    id: str = str(uuid4())
    email: EmailStr
    name: str
    app_secret_token: str = str(uuid4())
    website: str | None = None
