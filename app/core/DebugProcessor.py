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
            X = Mouse.position[0] // CellSize[0]
            Y = Mouse.position[1] // CellSize[1]
            self.text = f"{DateTime.date}|{(X, Y)}|{'MOUSEDOWN' if Mouse.button_down else ''}|{Keyboard.key}"
            self.text = self.text[-TerminalSize[0]*TerminalSize[1]:]
            Debug.text = self.text

