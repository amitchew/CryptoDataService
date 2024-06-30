# CryptoTradeAPI

CryptoTradeAPI is a FastAPI-based service that provides cryptocurrency trade and market data. It interacts with a PostgreSQL database to store and retrieve data about various cryptocurrencies.

## Deployed
https://cryptodataservice.onrender.com

## Features

- Store new trade data entries.
- Built with FastAPI and SQLAlchemy.

## Requirements

- Python 3.7+
- PostgreSQL

## Setup

### Clone the Repository

```bash
git clone https://github.com/amitchew/CryptoDataService.git

cd CryptoDataService

```

###  Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
###  Initialize the Database
```bash
python initialize_data.py
```
###  Run the Server
```bash
uvicorn main:app --reload
```
