import pygame
from pygame.event import Event
from core.interfaces import IGameEventProcessor
from core.KeyboardProcessor import Keyboard
from core.MouseProcessor import Mouse
from core.Globals import TerminalSize


class ExitProcessor(IGameEventProcessor):
    def process(self, event: Event) -> bool:
        if (
            event.type == pygame.QUIT
            or Keyboard.key == "Q"
            or (Mouse.button_down and Mouse.coordinates == (TerminalSize[0] - 1, 0))
        ):
            return True
        return False
