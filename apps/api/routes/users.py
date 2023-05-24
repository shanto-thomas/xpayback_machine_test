from fastapi import HTTPException, APIRouter, UploadFile, Request
from apps.api.schemas.users import UserRegistration
from apps.db.models.users import User, Profile
from apps.db.session import SessionLocal

router = APIRouter()


@router.post("/register")
def register_user(full_name: str, email: str, password: str, phone: str, profile_picture: UploadFile) -> dict:
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

    # Check if email already exists
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    # Check if phone already exists
    if db.query(User).filter(User.phone == user.phone).first():
        raise HTTPException(status_code=400, detail="Phone number already registered")
    # Create a new user record
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        phone=user.phone,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # Upload and save profile picture if provided
    if profile_picture:
        file_extension = user.profile_picture.filename.split(".")[-1]
        file_path = f"uploads/{new_user.id}.{file_extension}"
        with open(file_path, "wb") as f:
            f.write(profile_picture.file.read())
        # Create a profile record
        new_profile = Profile(
            user_id=new_user.id,
            profile_picture=file_path,
        )
        db.add(new_profile)
        db.commit()
    db.close()
    return dict(message="User registered successfully")


@router.get("/users/{user_id}")
def get_user(user_id: int, request: Request) -> dict:
    """
    Api for get user details
    """
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    db.close()
    return dict(id=user.id, full_name=user.full_name, email=user.email, phone=user.phone,
                profile_picture=f"{request.base_url}{profile.profile_picture}")
