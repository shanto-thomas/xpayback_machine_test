from fastapi import UploadFile
from pydantic import BaseModel


class UserRegistration(BaseModel):
    """ Request body model for user registration """

    full_name: str
    email: str
    password: str
    phone: str
    profile_picture: UploadFile
