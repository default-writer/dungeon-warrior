from core.interfaces import IGameEventProcessor
from core.DateTimeProcessor import DateTime
from core.MouseProcessor import Mouse
from core.KeyboardProcessor import Keyboard
from random import randrange
from core.Debug import Debug


alphabet = "qwertyuiopasdfghjklzxcvbnm0123456789"


class DemoProcessor(IGameEventProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.start_position: int = 0
        self.ticks = DateTime.ticks
        self.text = ""


    def process(self):
        if Debug.demo and self.ticks < DateTime.ticks:
            self.text += alphabet[randrange(len(alphabet))]
            self.ticks = DateTime.ticks
            Debug.text = self.text