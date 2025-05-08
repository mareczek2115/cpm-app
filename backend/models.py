from typing import List, Optional
from pydantic import BaseModel


class Event(BaseModel):
    id: int
    name: str
    duration: int
    predecessors: List[int]


class CpmNode(Event):
    early_start: Optional[int] = None
    early_finish: Optional[int] = None
    late_start: Optional[int] = None
    late_finish: Optional[int] = None
    reserve: Optional[int] = None
    successors: List[int] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)