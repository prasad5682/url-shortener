from pydantic import BaseModel

from pydantic import BaseModel, HttpUrl

class UrlCreate(BaseModel):
    original_url: HttpUrl


class UrlResponse(BaseModel):
    short_code: str

class StatsResponse(BaseModel):
    short_code: str
    total_clicks: int
