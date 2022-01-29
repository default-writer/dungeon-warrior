import pygame
from pygame import Color, Surface
from pygame.font import Font

from core.Globals import CellSize, ScreenSize, TerminalSize, TextAntialiasing


class Text:
    alphabet = " ~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?qwertyuiop[]asdfghjkl;'\zxcvbnm,./1234567890-="


class TextPainter:
    def __init__(self, font: Font):
        self.image = pygame.Surface((len(Text.alphabet) * CellSize[0], CellSize[1]))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        text_rects = []
        for ch in Text.alphabet:
            text_surface = font.render(ch, TextAntialiasing, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.top = 0
            text_rect.left = Text.alphabet.index(ch) * CellSize[0]
            text_rect.width = CellSize[0]
            text_rect.height = CellSize[1]
            text_rects.append(
                (text_surface, text_rect, (0, 0, CellSize[0], CellSize[1]))
            )
        self.image.blits(text_rects)

    def paint(self, text: str, surface: Surface) -> None:
        top: int = 0
        text_rects = []
        for line in [x if x else [] for x in text.split("|")]:
            if top + 1 > TerminalSize[1]:
                top = 0
            left: int = 0
            for ch in line:
                if left + 1 > TerminalSize[0]:
                    left = 0
                    top += 1
                text_rect = surface.get_rect()
                text_rect.top = top * CellSize[1]  # - 13
                text_rect.left = left * CellSize[0]
                text_rect.width = CellSize[0]
                text_rect.height = CellSize[1]
                text_rects.append(
                    (
                        self.image,
                        text_rect,
                        (
                            Text.alphabet.index(ch) * CellSize[0],
                            0,
                            CellSize[0],
                            CellSize[1],
                        ),
                    )
                )
                left += 1
            top += 1

        surface.blits(text_rects)
