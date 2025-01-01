from pydantic import BaseModel, HttpUrl

class Destination(BaseModel):
    account_id: str
    url: HttpUrl
    http_method: str
    headers: dict
