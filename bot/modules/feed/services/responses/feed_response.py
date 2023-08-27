from pydantic import BaseModel

from shared.my_types import Experiment


class FeedResponse(BaseModel):
    next_key: str | None
    items: list[Experiment]
