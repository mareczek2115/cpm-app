from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    name: str
    duration: int
    predecessors: List[int]
