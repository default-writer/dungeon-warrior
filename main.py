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


date_format = "%Y-%m-%d %H:%M:%S.%f"

class IGameState:
    def __init__(self):
        self.mouse_pos: tuple[int, int] = (0, 0)
        self.key = None
        self.debug: str = ""
        self.counter: int = 0


class IGameEventProcessor:
    def process(self):
        '''interface-only function'''
        pass
        

class MainScreenKeyboardProcessor(IGameEventProcessor):
    def __init__(self, game: IGameState):
        self.game = game
        
    def process(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.game.counter = self.game.counter + 1
            self.game.debug = f"UP{self.game.counter}"

        if keys[pygame.K_LEFT]:
            self.game.counter = self.game.counter + 1
            self.game.debug = f"LEFT{self.game.counter}"

        if keys[pygame.K_RIGHT]:
            self.game.counter = self.game.counter + 1
            self.game.debug = f"RIGHT{self.game.counter}"

        if keys[pygame.K_DOWN]:
            self.game.counter = self.game.counter + 1
            self.game.debug = f"DOWN{self.game.counter}"

        if keys[pygame.K_q]:
            self.game.run = False


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
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime(date_format)[:-3]
        self.icon = pygame.image.load(os.path.join("images", "dungeon.png"))
        self.font = pygame.font.Font(os.path.join("fonts", "pt-mono.ttf"), 16)
        self.keyboard_processor = MainScreenKeyboardProcessor(self)
        self.run = False

    def init(self) -> None:
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(self.icon)
        self.screen = pygame.display.set_mode(self.size, flags=pygame.NOFRAME, vsync=1)
        self.clock = pygame.time.Clock()
        self.date = datetime.fromtimestamp(self.ticks / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        self.text_surface = self.font.render(self.date, False, (0, 0, 0))
        self.state = GameStates.DRAW
        self.run = True
        print("Game started!")

    def quit(self) -> None:
        print("Game exited!")
        self.state = GameStates.QUIT
        pygame.quit()

    def draw(self) -> None:
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos != self.mouse_pos:
                        self.mouse_pos = mouse_pos
                        self.debug = f"{(self.mouse_pos[0], self.mouse_pos[1])}"

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos != self.mouse_pos:
                        self.mouse_pos = mouse_pos
                        self.debug = f"{(self.mouse_pos[0], self.mouse_pos[1])}"
                        
            self.keyboard_processor.process()

            self.paint()
            self.update()
            
            self.clock.tick(self.FPS)
            pygame.display.flip()

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


@decorator_factory(debug=True)
def main():
    game: Game = Game()
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
