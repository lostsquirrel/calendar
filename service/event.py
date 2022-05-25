from calendar import Calendar
from dataclasses import asdict
from datetime import datetime, timedelta

from dao.event import eventDAO
from db import transactional
from domain.calendar import CalendarItem, CalendarView
from domain.event import Event
from utils import format_date


def calendar_range(firstweekday: int, year: int, month: int):
    c = Calendar(firstweekday)
    return list(c.itermonthdates(year, month))


def list_range(firstweekday: int, calendar_id: int, year: int, month: int):
    time_range = calendar_range(firstweekday, year, month)
    rows = eventDAO.find_by_time_range(calendar_id,
                                       time_range[0],
                                       time_range[-1])
    items = {format_date(d): CalendarItem(date=d, events=[])
             for d in time_range}
    if rows is not None:
        events = [Event(*row) for row in rows]

        for event in events:

            end = event.end_date
            if end > time_range[-1]:
                end = time_range[-1]
            start = event.start_date
            if start < time_range[0]:
                start = time_range[0]
            delta = end - start
            for d in range(delta.days + 1):
                dd = start + timedelta(d)
                items[format_date(dd)].events.append(event.id)
    return CalendarView(events=events, items=items)


@transactional
def menstruation_start(calendar_id: int, start: datetime,
                       menstruation_period: int, full_period: int):

    end = start + timedelta(days=menstruation_period)

    full_period_delta = timedelta(days=full_period)
    # create current period
    menstruation_event = Event(
        id=None,
        title="经期",
        description="",
        calendar_id=calendar_id,
        create_time=datetime.now(),
        modified_time=datetime.now(),
        start_date=start,
        end_date=end,
        start_time=None,
        end_time=None,
        recurrence=0,
        state=1,
    )

    eventDAO.save(**asdict(menstruation_event))

    # predict ovulation preid
    ovulation_predict_delta = full_period / 2
    ovulation_start = ovulation_predict_delta - 5
    ovulation_end = ovulation_predict_delta + 4
    menstruation_event = Event(
        id=None,
        title="排卵期",
        description="",
        calendar_id=calendar_id,
        create_time=datetime.now(),
        modified_time=datetime.now(),
        start_date=start + timedelta(days=ovulation_start),
        end_date=start + timedelta(days=ovulation_end),
        start_time=None,
        end_time=None,
        recurrence=0,
        state=1,
    )
    eventDAO.save(**asdict(menstruation_event))
    # predict next period
    predict_menstruation = Event(
        id=None,
        title="经期(计算)",
        description="",
        calendar_id=calendar_id,
        create_time=datetime.now(),
        modified_time=datetime.now(),
        start_date=start + full_period_delta,
        end_date=end + full_period_delta,
        start_time=None,
        end_time=None,
        recurrence=0,
        state=1,
    )
    eventDAO.save(**asdict(predict_menstruation))


@transactional
def normal(calendar_id: int, title: str, description: str,
           start_date: str, end_date: str,
           start_time: str, end_time: str) -> int:
    event = Event(
        id=None,
        title=title,
        description=description,
        calendar_id=calendar_id,
        create_time=datetime.now(),
        modified_time=datetime.now(),
        start_date=start_date,
        end_date=end_date,
        start_time=start_time,
        end_time=None,
        recurrence=0,
        state=1,
    )
    return eventDAO.save(**asdict(event))
