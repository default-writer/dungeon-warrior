import pygame
from pygame import Surface
from pygame.event import Event


class IGameEventProcessor:
    def process(self, event: Event) -> bool:
        """interface-only function"""
        pass


class IGameProcessor:
    def process(self):
        """interface-only function"""
        pass


class ISurface:
    def __init__(self):
        self.surface: Surface = None
