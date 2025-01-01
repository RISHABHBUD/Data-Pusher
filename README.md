
# Overview
The **Data Pusher Application** is a Python-based API server built using **FastAPI**. It allows users to:

- Manage accounts and their associated destinations.
- Route data to multiple destinations based on account configurations.

# Features
### 1. **Account Management**
- Create, Read, Update, Delete (CRUD) operations for accounts.

### 2. **Destination Management**
- Create, Read, Update, Delete (CRUD) operations for destinations.
- Destinations are tied to specific accounts.

### 3. **Data Routing**
- Accepts incoming data via the `/server/incoming_data` endpoint.
- Routes data to all destinations configured for an account using their specific HTTP methods:
  - **GET**: Sends data as query parameters.
  - **POST** or **PUT**: Sends data as a JSON payload.
