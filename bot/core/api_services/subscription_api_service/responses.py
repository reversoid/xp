from typing import Literal
from core.models.subscription import Subscription
from pydantic import BaseModel


class GetSubscriptionStatusResponse(BaseModel):
    status: Literal["ACTIVE", "EXPIRED", "NO_SUBSCRIPTION"]
