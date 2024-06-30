import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

PORT=os.getenv("PORT")

database = Database(DATABASE_URL)
Base = declarative_base()

class CryptoData(Base):
    __tablename__ = "crypto_data"

    id = Column(Integer, primary_key=True, index=True)
    asset = Column(String, index=True)
    last_trade = Column(Float)
    change_24h_percent = Column(Float)
    change_24h = Column(Float)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class CryptoDataIn(BaseModel):
    asset: str
    last_trade: float
    change_24h_percent: float
    change_24h: float

class CryptoDataOut(CryptoDataIn):
    id: int

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/crypto_data/", response_model=CryptoDataOut)
async def create_crypto_data(data: CryptoDataIn):
    query = CryptoData.__table__.insert().values(
        asset=data.asset,
        last_trade=data.last_trade,
        change_24h_percent=data.change_24h_percent,
        change_24h=data.change_24h
    )
    last_record_id = await database.execute(query)
    return {**data.dict(), "id": last_record_id}

@app.get("/crypto_data/", response_model=List[CryptoDataOut])
async def read_crypto_data():
    query = CryptoData.__table__.select()
    return await database.fetch_all(query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)
