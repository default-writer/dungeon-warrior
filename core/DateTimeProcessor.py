import time
import pygame
from datetime import datetime, timedelta
from core.interfaces import IGameEventProcessor


date_format = "%Y-%m-%d %H:%M:%S"


class DateTime:
    date:str = ""


class DateTimeProcessor(IGameEventProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.time = pygame.time.get_ticks()
    def process(self):
        DateTime.date = f"{datetime.strftime(datetime(1, 1, 1, 0, 0, 0) + timedelta(seconds=pygame.time.get_ticks() // 1000), date_format)}"

