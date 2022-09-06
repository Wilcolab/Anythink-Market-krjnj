from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl, validator

from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    username: str


class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None

    @validator('image')
    def set_image(cls, image):
        return image or 'http://127.0.0.1:3000/static/images/placeholder.png'


class UserWithToken(User):
    token: str


class UserInResponse(RWSchema):
    user: UserWithToken
