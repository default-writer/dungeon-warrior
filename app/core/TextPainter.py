import pygame
from pygame import Color, Surface
from pygame.font import Font
from core.Globals import TerminalSize, CellSize, TextAntialiasing

class TextPainter:
    def paint(self, text: str, surface: Surface, font: Font) -> None:
        top: int = 0
        for line in [x if x else [] for x in text.split("|")]:
            if top + 1 > TerminalSize[1]:
                top = 0
            left: int = 0
            for ch in line:
                if left + 1 > TerminalSize[0]:
                    left = 0
                    top += 1
                text_surface = font.render(ch, TextAntialiasing, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.top = top * CellSize[1] - 13
                text_rect.left = left * CellSize[0]
                text_rect.width = CellSize[0]
                text_rect.height = CellSize[1]
                surface.blit(text_surface, text_rect)
                left += 1
            top += 1
