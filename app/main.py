from core.Globals import TerminalSize, CellSize
from core.DateTimeProcessor import DateTimeProcessor
from core.DebugProcessor import DebugProcessor
from core.DemoProcessor import DemoProcessor
from core.Game import Game
from core.MouseProcessor import MouseProcessor
from core.KeyboardProcessor import KeyboardProcessor
from core.ExitProcessor import ExitProcessor
from core.Utils import debugger


size = (TerminalSize[0]*CellSize[0], TerminalSize[1]*CellSize[1])


processors = [
    DateTimeProcessor(),
    DebugProcessor(),
    DemoProcessor()
    ]


event_processors = [
    KeyboardProcessor(),
    MouseProcessor()
    ]


exit_processor = ExitProcessor()


@debugger()
def main():
    game: Game = Game(
        size=size,
        processors=processors,
        event_processors=event_processors,
        exit_processor=exit_processor)
    game.init()
    game.draw()
    game.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
