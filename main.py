from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, UrlMapping, Click
from schemas import UrlCreate, UrlResponse, StatsResponse
from utils import generate_short_code

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/shorten", response_model=UrlResponse)
def shorten_url(data: UrlCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    while db.query(UrlMapping).filter_by(short_code=short_code).first():
        short_code = generate_short_code()

    url = UrlMapping(
        original_url=data.original_url,
        short_code=short_code
    )
    db.add(url)
    db.commit()
    db.refresh(url)

    return {"short_code": short_code}


@app.get("/{short_code}")
def redirect_url(short_code: str, request: Request, db: Session = Depends(get_db)):
    url = db.query(UrlMapping).filter_by(short_code=short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    click = Click(
        url_id=url.id,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    db.add(click)
    db.commit()

    return RedirectResponse(url=url.original_url, status_code=302)


@app.get("/api/stats/{short_code}", response_model=StatsResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    url = db.query(UrlMapping).filter_by(short_code=short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    total_clicks = db.query(Click).filter_by(url_id=url.id).count()

    return {
        "short_code": short_code,
        "total_clicks": total_clicks
    }
