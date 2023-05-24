# FastAPI User Registration and User Details API

This is a Python FastAPI code for a user registration and user details API. The API allows users to register with their information and retrieve user details, including the profile picture.

## Prerequisites

Make sure you have the following dependencies installed:

- [Python](https://www.python.org/) (version 3.7 or above)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your/repository.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database:

   - Ensure you have a PostgreSQL server running.
   - Create a new database named `user_data`.
   - Update the database connection URL in the code:

     ```python
     DATABASE_URL = "postgresql://postgres:123@localhost/user_data"
     ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Open your web browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the API documentation and interact with the endpoints.

## Endpoints

### User Registration

Register a new user with their information.

- **Endpoint**: `/register`
- **Method**: `POST`
- **Parameters**:
  - `full_name` (string): The full name of the user.
  - `email` (string): The email address of the user.
  - `password` (string): The password of the user.
  - `phone` (string): The phone number of the user.
  - `profile_picture` (file): The profile picture of the user (optional).
- **Response**:
  - `message` (string): A success message indicating that the user has been registered successfully.
- **Status Codes**:
  - `200`: User registered successfully.
  - `400`: Bad request. The email or phone number is already registered.

### Get User Details

Retrieve details of a specific user.

- **Endpoint**: `/users/{user_id}`
- **Method**: `GET`
- **Parameters**:
  - `user_id` (integer): The ID of the user.
- **Response**:
  - `id` (integer): The ID of the user.
  - `full_name` (string): The full name of the user.
  - `email` (string): The email address of the user.
  - `phone` (string): The phone number of the user.
  - `profile_picture` (string): The URL to retrieve the user's profile picture.
- **Status Codes**:
  - `200`: User details retrieved successfully.
  - `404`: User not found.

## Contributions

Contributions are welcome! If you find any issues or would like to add new features or improvements, please submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).