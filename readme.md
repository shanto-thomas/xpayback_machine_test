# FastAPI User Profile API

This is a Python FastAPI code for a user profile API. The API allows users to register, retrieve user information, and retrieve profile pictures.

## Prerequisites

Make sure you have the following dependencies installed:

- [Python](https://www.python.org/) (version 3.7 or above)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [uvicorn](https://www.uvicorn.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [pymongo](https://pymongo.readthedocs.io/)

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
   - Create a new database named `user_profile`.
   - Update the database connection URL in the code:

     ```python
     DATABASE_URL = "postgresql://postgres:123@localhost/user_profile"
     ```

4. Set up the MongoDB database:

   - Ensure you have a MongoDB server running.
   - Create a new database named `user_profile`.

5. Update the MongoDB configuration in the code:

   ```python
   mongo_host = "localhost"
   mongo_port = 27017
   mongo_database = "user_profile"
   ```

## Usage

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Open your web browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to access the API documentation and interact with the endpoints.

## Endpoints

### User Registration

Register a new user.

- **Endpoint**: `/registration/`
- **Method**: `POST`
- **Parameters**:
  - `full_name` (string): The full name of the user.
  - `phone` (string): The phone number of the user.
  - `email` (string): The email address of the user.
  - `profile_picture` (file): Optional. The profile picture of the user.
- **Response**:
  - `message` (string): A success message indicating that the user has been registered.
- **Status Codes**:
  - `201`: User registered successfully.
  - `400`: Bad request. The email address already exists.

### Get User Information

Retrieve information about a specific user.

- **Endpoint**: `/get_user/{user_id}`
- **Method**: `GET`
- **Parameters**:
  - `user_id` (string): The ID of the user.
- **Response**:
  - `user_id` (integer): The ID of the user.
  - `full_name` (string): The full name of the user.
  - `email` (string): The email address of the user.
  - `password` (string): The password of the user.
  - `phone` (string): The phone number of the user.
  - `pic` (string): The URL to retrieve the user's profile picture.
- **Status Codes**:
  - `200`: User information retrieved successfully.
  - `400`: Bad request. The user does not exist.

### Get Profile Picture

Retrieve the profile picture of a specific user.

- **Endpoint**: `/profile-picture/{user_id}`
- **Method**: `GET`
- **Parameters**:
  - `user

_id` (string): The ID of the user.
- **Response**:
  - The user's profile picture as an image/jpeg file.
- **Status Codes**:
  - `200`: Profile picture retrieved successfully.
  - `404`: Profile picture not found.
