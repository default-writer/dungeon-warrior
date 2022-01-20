import pygame
from pygame.event import Event
from core.interfaces import IGameEventProcessor


class Keyboard:
    key: str = ""


class KeyboardProcessor(IGameEventProcessor):
    def process(self, event: Event = None):
        if event:
            Keyboard.key = ""

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                Keyboard.key = "UP"

            if keys[pygame.K_LEFT]:
                Keyboard.key = "LEFT"

            if keys[pygame.K_RIGHT]:
                Keyboard.key = "RIGHT"

            if keys[pygame.K_DOWN]:
                Keyboard.key = "DOWN"

            if keys[pygame.K_q]:
                Keyboard.key = "Q"
