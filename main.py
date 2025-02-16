from fastapi import FastAPI

from fastapi.responses import Response


app = FastAPI()


@app.get("/")
async def read_root():
    """Just a test endpoint"""
    return {"Info": "This is a simple API, for Instagram account creation."}


@app.post("/create_account")
async def create_account(username: str, password: str) -> Response:
    """Automates the process of Instagram account creation."""
    return {"username": username, "password": password}
