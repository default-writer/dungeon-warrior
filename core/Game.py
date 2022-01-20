import os
import pygame
from typing import List

from core.interfaces import IGameProcessor, IGameEventProcessor
from core.KeyboardProcessor import Keyboard
from core.TextPainter import TextPainter
from core.DebugProcessor import Debug
from core.Utils import debugger


pygame.init()
pygame.font.init()


class Game:
    Fps = 60
    Caption = "Dungeon Warrior"
    Icon = pygame.image.load(os.path.join("images", "dungeon.png"))
    Font = pygame.font.Font(os.path.join("fonts", "pt-mono.ttf"), 64)

    def __init__(self, size: tuple[int, int] = (1920, 1080), processors: List[IGameProcessor] = None, event_processors: List[IGameEventProcessor] = None):
        self.event_processors: List[IGameEventProcessor] = event_processors
        self.processors: List[IGameProcessor] = processors
        self.surface: pygame.Surface = pygame.display.set_mode(size, flags=pygame.NOFRAME, vsync=1)
        self.painter:TextPainter = TextPainter()


    def init(self) -> None:
        pygame.display.set_caption(Game.Caption)
        pygame.display.set_icon(Game.Icon)
        self.clock = pygame.time.Clock()
        print("Game started!")

    def quit(self) -> None:
        pygame.quit()
        print("Game exited!")

    @debugger(raise_exception=False)
    def draw(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or Keyboard.key == "Q":
                    return
                for event_processor in self.event_processors:
                    event_processor.process(event)

            for processor in self.processors:
                processor.process()

            self.surface.fill((0, 0, 0))
            self.painter.paint(Debug.text, self.surface, Game.Font)

            self.clock.tick(Game.Fps)

            pygame.display.flip()
