from typing import List, Optional
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    name: str
    duration: int
    predecessors: List[int]


class CpmNode(Event):
    early_start: int = 0
    early_finish: int = 0
    late_start: int = 0
    late_finish: int = 0
    reserve: int = 0
    successors: List[int] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)