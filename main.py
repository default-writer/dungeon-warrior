from core.DateTimeProcessor import DateTimeProcessor
from core.Debug import DebugProcessor, DemoProcessor
from core.Game import Game
from core.MouseProcessor import MouseProcessor
from core.KeyboardProcessor import KeyboardProcessor
from core.Utils import debugger


processors = [
    DateTimeProcessor(),
    DebugProcessor(),
    DemoProcessor()
    ]


event_processors = [
    KeyboardProcessor(),
    MouseProcessor()
    ]


@debugger()
def main():
    game: Game = Game(
        processors=processors,
        event_processors=event_processors)
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
