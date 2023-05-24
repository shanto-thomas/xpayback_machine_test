from typing import Any

from fastapi import HTTPException, UploadFile, Request, APIRouter
from starlette.responses import Response

from apps.api.schemas.users import UserRegistration
from apps.db.models.users import UserInfo
from apps.db.session import SessionLocal, mongo_collection

router = APIRouter()


@router.post("/registration/")
async def register_user(full_name: str, email: str, password: str, phone: str, profile_picture: UploadFile) -> dict:
    """
    Api for user registration
    """
    db = SessionLocal()
    try:
        user = UserRegistration(full_name=full_name, email=email,
                                 password=password, phone=phone,
                                 profile_picture=profile_picture)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if db.query(UserInfo).filter(UserInfo.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    db_user = UserInfo(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    user_id = db_user.id
    profile_picture = user.profile_picture.file.read()
    mongo_collection.insert_one({"user_id": user_id, "profile_picture": profile_picture})

    return dict(message="User registered successfully")


@router.get("/get_user/{user_id}")
async def get_user(user_id: str, request: Request) -> dict:
    """
    Api for getting user details
    """
    db = SessionLocal()
    if db.query(UserInfo).filter(UserInfo.id == user_id).first():
        data = db.query(UserInfo).filter(UserInfo.id == user_id).first()
        return dict(user_id=data.id,
                    full_name=data.full_name,
                    email=data.email,
                    password=data.password,
                    phone=data.phone,
                    pic=f"{request.base_url}profile-picture/{data.id}")
    raise HTTPException(status_code=400, detail="Does not exists")


@router.get("/profile-picture/{user_id}")
async def get_profile_picture(user_id: str) -> Response:
    """
    Api for getting user profile picture
    """
    # Retrieve the profile picture from MongoDB based on the user_id
    picture_data = mongo_collection.find_one({'user_id': int(user_id)})

    if picture_data:
        picture_bytes = picture_data['profile_picture']
        return Response(content=picture_bytes, media_type='image/jpeg')
    else:
        return dict(message= "Profile picture not found")
