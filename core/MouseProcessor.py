import pygame
from pygame.event import Event
from core.interfaces import IGameEventProcessor


class Mouse:
    position: tuple[int, int] = (0, 0)
    button_down: bool = False


class MouseProcessor(IGameEventProcessor):
    def process(self, event: Event = None):
        if event:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                Mouse.position = mouse_pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse.button_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                Mouse.button_down = False
