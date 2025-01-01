from fastapi import APIRouter, HTTPException
from models.account import Account
from database import accounts_db

router = APIRouter()

@router.post("/accounts/")
def create_account(account: Account):
    if any(acc.email == account.email for acc in accounts_db):
        raise HTTPException(status_code=400, detail="Email already exists")
    accounts_db.append(account)
    return {"message": "Account created successfully", "account": account}

@router.get("/accounts/{account_id}")
def get_account(account_id: str):
    for account in accounts_db:
        if account.id == account_id:
            return account
    raise HTTPException(status_code=404, detail="Account not found")

@router.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    global accounts_db
    accounts_db = [acc for acc in accounts_db if acc.id != account_id]
    return {"message": "Account deleted"}
