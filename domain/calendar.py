from dataclasses import dataclass
from datetime import datetime, date
from typing import List
from domain.event import Event

from domain.user import User


@dataclass
class Calendar:
    id: int
    name: str
    user: User
    create_time: datetime
    modified_time: datetime
    state: int


@dataclass
class CalendarItem:
    date: date
    events: List[int]


@dataclass
class CalendarView:
    events: List[Event]
    items: List[CalendarItem]
