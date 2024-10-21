# FastAPI CRUD Operations Project

This project demonstrates how to create a simple CRUD (Create, Read, Update, Delete) API using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.9.13
- pip (Python package installer)
- PostgreSQL

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/PritamIT2023/crud-FASTAPI-poc.git
   cd fastapi-crud-project
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your database:
   
   This project uses PostgreSQL. Make sure you have PostgreSQL installed and running. Then, create a new database for this project.

   The database connection is configured using the following URL:

   ```python
   SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/python-fast"
   ```

   This URL is structured as follows:
   - `postgresql://`: The database system being used
   - `postgres`: The username for the database
   - `admin`: The password for the database user
   - `localhost:5432`: The host and port where the database server is running
   - `python-fast`: The name of the database

   Modify this URL in your `database.py` file if your PostgreSQL setup is different.

4. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

## Project Structure

```
fastapi-crud-project/
│
├──db
│   ├── Models.py
│   ├── database.py
|   ├── schema.py
├── main.py
├── requirements.txt
└── README.md
```

- `main.py`: Contains the FastAPI application and route definitions.
- `Models.py`: Contains model structure.
- `schema.py`: Defines the Pydantic models for request/response handling.
- `database.py`: Handles database connections and operations.
- `requirements.txt`: Lists all the Python dependencies for the project.

## API Endpoints

- `GET /product`: Retrieve all product
- `GET /product/{product_id}`: Retrieve a specific item
- `POST /product`: Create a new item
- `PUT /product/{product_id}`: Update an existing item
- `DELETE /product/{product_id}`: Delete an item


## Run the Application

Run your application :

```bash
fastapi dev main.py
```

Auto-reloading when code changes are detected.


## Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
