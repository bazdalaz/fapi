
from pydantic import BaseModel

class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
    user_id: int
    title: str
