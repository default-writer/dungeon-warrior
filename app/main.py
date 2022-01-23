import sys
import os
from core.DateTimeProcessor import DateTimeProcessor
from core.DebugProcessor import DebugProcessor
from core.DemoProcessor import DemoProcessor
from core.Game import Game
from core.MouseProcessor import MouseProcessor
from core.KeyboardProcessor import KeyboardProcessor
from core.Utils import debugger


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))


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
