from fastapi import FastAPI
from routes import account_routes , destination_routes , data_handler

app = FastAPI()

app.include_router(account_routes.router, prefix="/api")
app.include_router(destination_routes.router, prefix="/api")
app.include_router(data_handler.router, prefix="/api")
