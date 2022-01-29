import time
from datetime import datetime, timedelta

import pygame

from core.interfaces import IGameEventProcessor

date_format = "%Y-%m-%d %H:%M:%S"


class DateTime:
    date: str = ""
    ticks: int = 0


class DateTimeProcessor(IGameEventProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.time = pygame.time.get_ticks()

    def process(self):
        ticks = pygame.time.get_ticks() // 1000
        DateTime.date = f"{datetime.strftime(datetime(1, 1, 1, 0, 0, 0) + timedelta(seconds=ticks), date_format)}"
        if DateTime.ticks != ticks:
            DateTime.ticks = DateTime.ticks + 1
