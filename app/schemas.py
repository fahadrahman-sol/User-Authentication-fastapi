# schemas.py
from pydantic import BaseModel, EmailStr

from pydantic import BaseModel

# User login schema (request body for login)
class LoginSchema(BaseModel):
    email: str
    password: str

# Token schema (response body for returning the token)
class TokenSchema(BaseModel):
    access_token: str
    token_type: str

# User creation schema (request body for user registration)
class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str

# User response schema (response body for user data)
class UserResponse(BaseModel):
    email: str
    full_name: str
