import os
import sys
from core import Game

def pytest_configure(config):
    config.game = Game()