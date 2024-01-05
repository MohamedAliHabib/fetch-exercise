"""Sets up multi-level file logger for information and errors."""

import logging
import sys
from enum import Enum

class Levels(Enum):
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

class Logger:
    def __init__(self, name: str, level: Levels = Levels.INFO, filename: str = 'app.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.value) 
        self._setup_handler(filename)

    def _setup_handler(self, filename):
        # console_handler = logging.StreamHandler(sys.stdout)
        console_handler = logging.FileHandler(filename)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(console_handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)