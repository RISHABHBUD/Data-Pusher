from fastapi import APIRouter, HTTPException, Request
import requests
from database import accounts_db, destinations_db

router = APIRouter()

@router.post("/server/incoming_data")
async def handle_incoming_data(request: Request):
    headers = request.headers
    data = await request.json()

    app_secret_token = headers.get("CL-XTOKEN")
    if not app_secret_token:
        return {"message": "Un Authenticate"}

    account = next((acc for acc in accounts_db if acc.app_secret_token == app_secret_token), None)
    if not account:
        return {"message": "Un Authenticate"}

    account_destinations = [dest for dest in destinations_db if dest.account_id == account.id]
    for destination in account_destinations:
        if destination.http_method.upper() == "GET":
            response = requests.get(destination.url, params=data, headers=destination.headers)
        elif destination.http_method.upper() in ["POST", "PUT"]:
            response = requests.request(destination.http_method.upper(), destination.url, json=data, headers=destination.headers)
        else:
            raise HTTPException(status_code=400, detail="Unsupported HTTP method")

    return {"message": "Data sent successfully"}
