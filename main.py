from core.DateTimeProcessor import DateTimeProcessor
from core.DebugProcessor import DebugProcessor
from core.Game import Game
from core.MouseProcessor import MouseProcessor, Mouse
from core.KeyboardProcessor import KeyboardProcessor, Keyboard
from core.Utils import debugger


processors = [
    DateTimeProcessor(),
    DebugProcessor()]


event_processors = [
    KeyboardProcessor(),
    MouseProcessor()]


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
