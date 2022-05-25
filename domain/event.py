from dataclasses import dataclass
from datetime import datetime, date, time


@dataclass
class Event:
    id: int
    title: str
    description: str
    calendar_id: int
    create_time: datetime
    modified_time: datetime
    start_date: date
    end_date: date
    start_time: time
    end_time: time
    recurrence: int
    state: int
