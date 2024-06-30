import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

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

def get_initial_data():
    return [
        {"asset": "BTC/USD", "last_trade": 63000.00, "change_24h_percent": -2.21, "change_24h": -1426.18},
        {"asset": "ETH/USD", "last_trade": 3408.90, "change_24h_percent": -0.33, "change_24h": -11.20},
        {"asset": "DOGE/USD", "last_trade": 0.15, "change_24h_percent": 15.75, "change_24h": 0.02},
        {"asset": "ALGO/USD", "last_trade": 0.15, "change_24h_percent": 0.00, "change_24h": 0.00},
        {"asset": "DOT/USD", "last_trade": 5.64, "change_24h_percent": 0.00, "change_24h": 0.00},
        {"asset": "UNI/USD", "last_trade": 9.79, "change_24h_percent": 0.00, "change_24h": 0.00},
        {"asset": "COMP/USD", "last_trade": 45.67, "change_24h_percent": -0.95, "change_24h": -0.44},
    ]

def initialize_data():
    session = SessionLocal()
    try:
        data = get_initial_data()
        for item in data:
            crypto_data = CryptoData(**item)
            session.add(crypto_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    initialize_data()
    print("Data has been initialized.")
