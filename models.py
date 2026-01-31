from pydantic import BaseModel, Field, EmailStr


class Post(BaseModel):
    userId: int = Field(gt=0)
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    body: str = Field(min_length=1)


class Comment(BaseModel):
    postId: int = Field(gt=0)
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    email: EmailStr
    body: str = Field(min_length=1)