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
            Keyboard.key = f"UP"

        if keys[pygame.K_LEFT]:
            Keyboard.key = f"LEFT"

        if keys[pygame.K_RIGHT]:
            Keyboard.key = f"RIGHT"

        if keys[pygame.K_DOWN]:
            Keyboard.key = f"DOWN"

        if keys[pygame.K_q]:
            Keyboard.key = "Q"


class MainScreenDebugProcessor(IGameEventProcessor):
    def process(self):
        Text.debug = f"{(Mouse.position[0], Mouse.position[1])} {'DOWN' if Mouse.button_down else ''} {Keyboard.key}"

class Painter:
    def __init__(self, size:tuple[int, int]):
        self.size = size
        self.ticks = Game.ticks_ms()
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        self.text_surface = Game.font.render(self.date, False, (0, 0, 0))
        self.screen = pygame.display.set_mode(self.size, flags=pygame.NOFRAME, vsync=1)

    def paint(self) -> None:
        self.date = datetime.fromtimestamp(Game.ticks_ms() / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        text_surface = Game.font.render(Text.debug, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        self.screen.fill((0, 0, 0))
        self.screen.blit(text_surface, text_rect)


class Game:
    fps = 60
    caption = "Dungeon Warrior"
    icon = pygame.image.load(os.path.join("images", "dungeon.png"))
    font = pygame.font.Font(os.path.join("fonts", "pt-mono.ttf"), 64)

    def __init__(self, size: tuple[int, int] = (1920, 1080)):
        pygame.display.set_caption(Game.caption)
        pygame.display.set_icon(Game.icon)
        self.clock = pygame.time.Clock()
        self.mouse_processor = MainScreenMouseProcessor()
        self.keyboard_processor = MainScreenKeyboardProcessor()
        self.debug_processor = MainScreenDebugProcessor()
        self.painter = Painter(size)


    def init(self) -> None:
        print("Game started!")

    def quit(self) -> None:
        print("Game exited!")
        pygame.quit()

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
            self.debug_processor.process()
            self.painter.paint()

            self.clock.tick(Game.fps)

            pygame.display.flip()

    @staticmethod
    def ticks_ms() -> int:
        return int(round(time.time() * 1000))

@decorator_factory(debug=True)
def main():
    game: Game = Game()
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
