"""
This file performs the following:
- Configures the argument parser responsible of taking the input file path as an argument - through a user prompt in terminal.
- Reads the contents of the file and returns them as a list of strings representing the lines.
"""
from argparser import ArgumentParser
from logger import Logger, Levels

logger = Logger(name=__name__, level=Levels.INFO)

class Reader():
    def __init__(self) -> None:
        args = self.get_args()
        self.file_path = args.endpoints_file

    def get_args(self):
        file_parser = ArgumentParser()
        args = file_parser.parse()
        return args

    def read_file(self) -> list[str]:
        try:
            logger.info(f'Reading data from file: {self.file_path}')
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = f.read()
                return data.splitlines() # return as a list of text lines
        except FileNotFoundError:
            msg = f"The file at {self.file_path} was not found."
            logger.error(msg)
            raise FileNotFoundError(msg)
        except IOError as e:
            msg = f"An error occurred while reading the file: {e}"
            logger.error(msg)
            raise IOError(msg)
