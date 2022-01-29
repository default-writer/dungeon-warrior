import pygame
from core.Globals import CellSize
from core.interfaces import IGameEventProcessor
from pygame.event import Event


class Mouse:
    position: tuple[int, int] = (0, 0)
    coordinates: tuple[int, int] = (0, 0)
    button_down: bool = False


class MouseProcessor(IGameEventProcessor):
    def process(self, event: Event = None) -> bool:
        if event:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                Mouse.position = mouse_pos
                Mouse.coordinates = (
                    Mouse.position[0] // CellSize[0],
                    Mouse.position[1] // CellSize[1],
                )
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse.button_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                Mouse.button_down = False
            return True
        return False
