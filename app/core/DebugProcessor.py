from core.interfaces import IGameEventProcessor
from core.DateTimeProcessor import DateTime
from core.MouseProcessor import Mouse
from core.KeyboardProcessor import Keyboard
from core.Globals import CellSize
from random import randrange
from core.Debug import Debug
from core.Globals import TerminalSize


class DebugProcessor(IGameEventProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.text = ""

    def process(self):
        if not Debug.demo:
            self.text = f"{DateTime.date}|{Mouse.coordinates}|{'MOUSEDOWN' if Mouse.button_down else ''}|{Keyboard.key}"
            self.text = self.text[-TerminalSize[0] * TerminalSize[1] :]
            Debug.text = self.text
