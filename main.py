import os.path
import time
from datetime import datetime
import pygame


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


class IGameState:
    def __init__(self):
        self.mouse_pos: tuple[int, int] = (0, 0)
        self.key = None
        self.debug: str = ""
        self.counter: int = 0
        self.dirty: bool = True


class Game(IGameState):
    def __init__(self, size: tuple[int, int] = (1920, 1080)):
        super().__init__()
        pygame.init()
        pygame.font.init()
        self.caption = "Dungeon Warrior"
        self.size = size
        self.FPS = 60
        self.state = GameStates.INIT
        self.ticks = Game.ticks_ms()
        self.font = None
        self.icon = None
        self.screen = None
        self.clock = None
        self.text_surface = None
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        self.icon = pygame.image.load(os.path.join("images", "dungeon.png"))
        self.font = pygame.font.Font(os.path.join("fonts", "pt-mono.ttf"), 64)

    def init(self) -> None:
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode(self.size, flags=pygame.SCALED | pygame.RESIZABLE, vsync=1)
        self.clock = pygame.time.Clock()
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        self.text_surface = self.font.render(self.date, False, (0, 0, 0))
        print("Game started!")

    def quit(self) -> None:
        print("Game exited!")
        self.state = GameStates.QUIT
        pygame.quit()

    def draw(self) -> None:
        while True:
            state: int = Game.event_loop(self)
            if state == GameStates.QUIT:
                return
            if state == GameStates.INIT:
                self.init()
            if state == GameStates.DRAW:
                self.paint()
            if self.dirty:
                self.update()
                self.clock.tick(self.FPS)
                pygame.display.flip()
                self.dirty = False

    def text_objects(self, text, font):
        self.text_surface = font.render(text, True, (255, 255, 255))
        return self.text_surface, self.text_surface.get_rect()

    def update(self):
        self.ticks = Game.ticks_ms()
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def paint(self) -> None:
        text_surface, text_rect = self.text_objects(self.debug, self.font)
        # x = 0
        # y = 0
        # w = text_rect.width
        # h = text_rect.height
        # text_rect.center = ((x + (w/2)), (y + (h/2)))
        self.screen.fill((0, 0, 0))
        self.screen.blit(text_surface, text_rect)

    @staticmethod
    def ticks_ms() -> int:
        return int(round(time.time() * 1000))

    @staticmethod
    def event_loop(gs: IGameState) -> int:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameStates.QUIT

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos != gs.mouse_pos:
                    gs.mouse_pos = mouse_pos
                    gs.dirty = True
                    gs.debug = f"{(gs.mouse_pos[0], gs.mouse_pos[1])}"
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                gs.key = key
                if key[pygame.K_UP]:
                    gs.counter = gs.counter + 1
                    gs.debug = f"UP{gs.counter}"
                    gs.dirty = True
                if key[pygame.K_LEFT]:
                    gs.counter = gs.counter + 1
                    gs.debug = f"LEFT{gs.counter}"
                    gs.dirty = True
                if key[pygame.K_RIGHT]:
                    gs.counter = gs.counter + 1
                    gs.debug = f"RIGHT{gs.counter}"
                    gs.dirty = True
                if key[pygame.K_DOWN]:
                    gs.counter = gs.counter + 1
                    gs.debug = f"DOWN{gs.counter}"
                    gs.dirty = True

        return GameStates.DRAW


@decorator_factory(debug=True)
def main():
    game: Game = Game()
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
