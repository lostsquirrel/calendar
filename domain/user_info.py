

from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserInfo:

    id: int
    user_id: int
    pregnancy: int
    menstruation_period: int
    full_period: int
    firstweekday: int
    create_time: datetime
    modified_time: datetime
    state: int
