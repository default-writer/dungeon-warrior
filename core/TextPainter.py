import pygame
from pygame import Surface
from pygame.font import Font


class TextPainter:
    def paint(self, text: str, surface: Surface, font: Font) -> None:
        top: int = 0
        for line in text.split("|"):
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.top = top
            text_rect.left = 0
            top += text_rect.height
            surface.blit(text_surface, text_rect)