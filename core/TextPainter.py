import pygame
from pygame import Surface
from pygame.font import Font
from core.Globals import TerminalSize, CellSize, TextAntialiasing

class TextPainter:
    def paint(self, text: str, surface: Surface, font: Font) -> None:
        top: int = 0
        for line in [x if x else [] for x in text.split("|")]:
            if top < TerminalSize[1]:
                left: int = 0
                for ch in line:
                    text_surface = font.render(ch, TextAntialiasing, (255, 255, 255))
                    text_rect = text_surface.get_rect()
                    text_rect.top = top * CellSize[1]
                    text_rect.left = left * CellSize[0]
                    text_rect.width = CellSize[0]
                    text_rect.height = CellSize[1]
                    if left < TerminalSize[0]:
                        surface.blit(text_surface, text_rect)
                        left += 1
                    else:
                        left = 0
                        top += 1
                top += 1
