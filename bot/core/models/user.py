from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    tgId: str
    tgUsername: str
    createdAt: datetime
