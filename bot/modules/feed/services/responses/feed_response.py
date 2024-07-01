from pydantic import BaseModel

from shared.models import Experiment


class FeedResponse(BaseModel):
    next_key: str | None
    items: list[Experiment]
