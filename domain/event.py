from dataclasses import dataclass
from datetime import datetime, date, time, timedelta


def timedelta_to_time(s: timedelta) -> time:
    return (datetime.min + s).time()


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

    def __post_init__(self):
        if self.start_time is not None:
            if isinstance(self.start_time, timedelta):
                self.start_time = timedelta_to_time(self.start_time)
        if self.end_time is not None and isinstance(self.end_time, timedelta):
            self.end_time = timedelta_to_time(self.end_time)
