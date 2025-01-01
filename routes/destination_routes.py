from fastapi import APIRouter, HTTPException
from models.destination import Destination
from database import destinations_db

router = APIRouter()

@router.post("/destinations/")
def create_destination(destination: Destination):
    destinations_db.append(destination)
    return {"message": "Destination added"}

@router.get("/destinations/{account_id}")
def get_destinations(account_id: str):
    account_destinations = [dest for dest in destinations_db if dest.account_id == account_id]
    if not account_destinations:
        raise HTTPException(status_code=404, detail="No destinations found")
    return account_destinations
