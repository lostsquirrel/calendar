from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    create_time: datetime
    modified_time: datetime
    state: int



