from pydantic import BaseModel

class UrlCreate(BaseModel):
    original_url: str

class UrlResponse(BaseModel):
    short_code: str

class StatsResponse(BaseModel):
    short_code: str
    total_clicks: int
