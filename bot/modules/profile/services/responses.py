from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    tg_id: int
    username: str


class PaginatedUsersResponse(BaseModel):
    next_key: str | None = None
    items: list[UserResponse]
