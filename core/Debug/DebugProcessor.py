from core.interfaces import IGameEventProcessor
from core.DateTimeProcessor import DateTime
from core.MouseProcessor import Mouse
from core.KeyboardProcessor import Keyboard
from core.Globals import CellSize
from random import randrange
from core.Debug import Debug


class DebugProcessor(IGameEventProcessor):
    def process(self):
        if not Debug.demo:
            X = Mouse.position[0] // CellSize[0]
            Y = Mouse.position[1] // CellSize[1]
            Debug.text = f"{DateTime.date}|{(X, Y)}|{'MOUSEDOWN' if Mouse.button_down else ''}|{Keyboard.key}"

