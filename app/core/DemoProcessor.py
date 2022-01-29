from core.interfaces import IGameEventProcessor
from core.DateTimeProcessor import DateTime
from core.Globals import TerminalSize
from core.Debug import Debug


class Demo:
    alphabet = "qwertyuiopasdfghjklzxcvbnm0123456789"


class DemoProcessor(IGameEventProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.start_position: int = 0
        self.ticks = DateTime.ticks
        self.text = ""
        self.state = 0

    def process(self):
        if Debug.demo:  # and self.ticks < DateTime.ticks:
            # self.text += alphabet[randrange(len(alphabet))]
            self.text += Demo.alphabet[self.state]
            # self.ticks = DateTime.ticks
            self.state += 1
            self.state %= len(Demo.alphabet)
            self.text = self.text[-TerminalSize[0] * TerminalSize[1] :]
            Debug.text = self.text
