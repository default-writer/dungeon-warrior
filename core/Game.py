import os
import pygame
from pygame import Surface
from typing import List
from core.Globals import TerminalSize, CellSize
from core.interfaces import IGameProcessor, IGameEventProcessor
from core.KeyboardProcessor import Keyboard
from core.TextPainter import TextPainter
from core.Debug.DebugProcessor import Debug
from core.Utils import debugger
from core.Globals import Caption, Fps

pygame.init()
pygame.font.init()


class Game:
    Icon = pygame.image.load(os.path.join("images", "dungeon.png"))
    Font = pygame.font.Font(os.path.join("fonts", "SourceCodePro-Regular.ttf"), CellSize[1])

    def __init__(self,
                 size: tuple[int, int] = (TerminalSize[0]*CellSize[0], TerminalSize[1]*CellSize[1]),
                 processors: List[IGameProcessor] = None,
                 event_processors: List[IGameEventProcessor] = None):
        self.event_processors: List[IGameEventProcessor] = event_processors
        self.processors: List[IGameProcessor] = processors
        self.surface: Surface = pygame.display.set_mode(size, flags=pygame.NOFRAME, vsync=1)
        self.painter:TextPainter = TextPainter()


    def init(self) -> None:
        pygame.display.set_caption(Caption)
        pygame.display.set_icon(Game.Icon)
        self.clock = pygame.time.Clock()
        print("Game started!")

    def quit(self) -> None:
        pygame.quit()
        print("Game exited!")

    @debugger(raise_exception=True)
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

            self.clock.tick(Fps)

            pygame.display.flip()
