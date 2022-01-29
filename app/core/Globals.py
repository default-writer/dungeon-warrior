Fps = 60
Caption = "Dungeon Warrior"
TerminalSize = (80, 24)  # width = 1920 = 80*24, height = 1080 = 24*45
CellSize = (24, 45)  # width = 24, height = 45
ScreenSize = (TerminalSize[0] * CellSize[0], TerminalSize[1] * CellSize[1])
TextAntialiasing = True

# Screen text resolution is 80x24 in text mode
# Screen resolution in graphical mode is 1920x1080
# X range is from 0 to 1919
# Y range is from 0 to 1079
# TODO: show in debug string text mode coordinates
