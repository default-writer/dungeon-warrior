import time
from datetime import datetime
from core.interfaces import IGameEventProcessor


date_format = "%Y-%m-%d %H:%M:%S.%f"


class DateTime:
    date:str = ""


class DateTimeProcessor(IGameEventProcessor):
    def process(self):
        DateTime.date = f"{datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}"

