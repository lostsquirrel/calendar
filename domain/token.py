
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Token:

    id: int
    token: str
    user_id: int
    create_time: datetime
    modified_time: datetime
    state: int
