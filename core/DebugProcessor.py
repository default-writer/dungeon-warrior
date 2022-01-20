from core.interfaces import IGameEventProcessor
from core.DateTimeProcessor import DateTime
from core.MouseProcessor import Mouse
from core.KeyboardProcessor import Keyboard


class Debug:
    text: str = ""


class DebugProcessor(IGameEventProcessor):
    def process(self):
        Debug.text = f"{DateTime.date}|{(Mouse.position[0], Mouse.position[1])}|{'MOUSEDOWN' if Mouse.button_down else ''}|{Keyboard.key}"
