from pydantic import BaseModel


class RegisterUserDto(BaseModel):
    tgId: int
    tgUsername: str
