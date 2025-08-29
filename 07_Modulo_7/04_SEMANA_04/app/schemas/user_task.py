from pydantic import BaseModel, Field
from typing import Annotated

class UserCreate(BaseModel):
    username: Annotated[str, Field(min_length=4, max_length=20)]
    password: Annotated[str, Field(min_length=6)]
    role: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token :str
    Token_type: str

class LoginForm(BaseModel):
    username: str
    password: str

