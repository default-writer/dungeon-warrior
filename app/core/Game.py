import os
import pygame
import pygame.font
from pygame import Surface
from pygame.font import Font
from typing import List
from core.MouseProcessor import Mouse
from core.Globals import CellSize, ScreenSize
from core.interfaces import IGameProcessor, IGameEventProcessor
from core.KeyboardProcessor import Keyboard
from core.TextPainter import TextPainter
from core.DebugProcessor import Debug
from core.Utils import debugger
from core.Globals import Caption, Fps

import OpenGL.GL as gl
import OpenGL.GLU as glut

pygame.init()
pygame.font.init()


class Game:
    Icon = pygame.image.load(os.path.join("images", "dungeon.png"))
    Font: Font = Font(os.path.join("fonts", "SourceCodePro-Regular.ttf"), CellSize[1])

    def __init__(self,
                 size: tuple[int, int], # = (TerminalSize[0]*CellSize[0], TerminalSize[1]*CellSize[1]),
                 processors: List[IGameProcessor],
                 event_processors: List[IGameEventProcessor],
                 exit_processor: IGameEventProcessor):
        self.exit_processor: IGameEventProcessor = exit_processor
        self.event_processors: List[IGameEventProcessor] = event_processors
        self.processors: List[IGameProcessor] = processors
        self.size = size
        self.surface: Surface = pygame.display.set_mode(size, flags=pygame.NOFRAME | pygame.DOUBLEBUF | pygame.OPENGL, vsync=1)
        self.painter:TextPainter = TextPainter()


    def init(self) -> None:
        pygame.display.set_caption(Caption)
        pygame.display.set_icon(Game.Icon)
        self.clock = pygame.time.Clock()
        glut.gluPerspective(45, (ScreenSize[0]/ScreenSize[1]), 0.1, 50.0)
        gl.glTranslatef(0.0, 0.0, -2.65)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
        print("Game started!")

    def quit(self) -> None:
        pygame.quit()
        print("Game exited!")

    @debugger(raise_exception=True)
    def draw(self) -> None:
        while True:
            for event in pygame.event.get():
                if self.exit_processor.process(event):
                    return
                for event_processor in self.event_processors:
                    event_processor.process(event)

            for processor in self.processors:
                processor.process()

            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

            self.painter.paint(Debug.text, self.surface, Game.Font)
            self.clock.tick(Fps)

            pygame.display.flip()
