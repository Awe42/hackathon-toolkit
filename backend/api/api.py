from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import Database

db = Database()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/add/{table}')
async def add(table: str, data: Request):
    """Add Data to Postgres Database
    Args:
        data (List[List]): List containing name and diagnostic for all patients
    """
    form = await data.body()
    data_string = form.decode(encoding='utf-8')
    decoded = data_string.replace('"', '').split(',')
    print(decoded)
    db.add(table, decoded)

@app.get('/read')
async def readTables():
    return db.table_names

@app.get('/read/{table}')
async def read(table: str):
    """Get data from database

    Returns:
        data: data stored in Postgres database
    """
    data = db.read(table)
    return data
