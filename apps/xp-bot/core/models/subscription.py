from datetime import datetime
from pydantic import BaseModel


class Subscription(BaseModel):
    createdAt: datetime
    until: datetime
