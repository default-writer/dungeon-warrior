import pygame
from pygame.event import Event
from core.Debug import Debug
from core.interfaces import IGameEventProcessor
from core.Debug import Debug

class Keyboard:
    key: str = ""


class KeyboardProcessor(IGameEventProcessor):
    def process(self, event: Event = None)->bool:
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

            if keys[pygame.K_d]:
                Keyboard.key = ""
                Debug.demo = True

            if keys[pygame.K_f]:
                Keyboard.key = ""
                Debug.demo = False
            return True
        return False

