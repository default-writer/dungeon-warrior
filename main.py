import os.path
import time
from datetime import datetime
import pygame


pygame.init()
pygame.font.init()


def decorator_factory(debug=False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except Exception as ex:
                if debug:
                    raise ex
        return wrapper
    return decorator


class GameStates:
    INIT = 1
    DRAW = 2
    QUIT = 4


date_format = "%Y-%m-%d %H:%M:%S.%f"


class IGameEventProcessor:
    def process(self):
        '''interface-only function'''
        pass


class Mouse:
    position: tuple[int, int] = (0, 0)
    button_down: bool = False


class Keyboard:
    key: str = ""


class Text:
    debug: str = ""


class DateTime:
    date:str = ""


class MainScreenMouseProcessor(IGameEventProcessor):
    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        if Mouse.position != mouse_pos:
            Mouse.position = mouse_pos


class MainScreenKeyboardProcessor(IGameEventProcessor):
    def process(self):
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


class MainScreenDateTimeProcessor(IGameEventProcessor):
    def process(self):
        DateTime.date = f"{datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}"


class MainScreenDebugProcessor(IGameEventProcessor):
    def process(self):
        Text.debug = f"{DateTime.date}|{(Mouse.position[0], Mouse.position[1])}|{'MOUSEDOWN' if Mouse.button_down else ''}|{Keyboard.key}"


class ISurface(pygame.Surface):
    def __init__(self, surface: pygame.Surface):
        self.surface = surface


class Painter:
    def paint(self, surface: ISurface) -> None:
        surface.surface.fill((0, 0, 0))
        top: int = 0
        for line in Text.debug.split("|"):
            text_surface = Game.font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.top = top
            text_rect.left = 0
            top += text_rect.height
            surface.surface.blit(text_surface, text_rect)


class Game(ISurface):
    fps = 60
    caption = "Dungeon Warrior"
    icon = pygame.image.load(os.path.join("images", "dungeon.png"))
    font = pygame.font.Font(os.path.join("fonts", "pt-mono.ttf"), 64)

    def __init__(self, size: tuple[int, int] = (1920, 1080)):
        super().__init__(pygame.display.set_mode(size, flags=pygame.NOFRAME, vsync=1))
        self.keyboard_processor = MainScreenKeyboardProcessor()
        self.mouse_processor = MainScreenMouseProcessor()
        self.datetime_processor = MainScreenDateTimeProcessor()
        self.debug_processor = MainScreenDebugProcessor()
        self.painter = Painter()

    def init(self) -> None:
        pygame.display.set_caption(Game.caption)
        pygame.display.set_icon(Game.icon)
        self.clock = pygame.time.Clock()
        print("Game started!")

    def quit(self) -> None:
        pygame.quit()
        print("Game exited!")

    def draw(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or Keyboard.key == "Q":
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Mouse.button_down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    Mouse.button_down = False

            self.keyboard_processor.process()
            self.mouse_processor.process()
            self.datetime_processor.process()
            self.debug_processor.process()
            self.painter.paint(self)
            self.clock.tick(Game.fps)

            pygame.display.flip()


@decorator_factory(debug=True)
def main():
    game: Game = Game()
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
