"""Configures the argument parses that reads the file path from terminal."""
import argparse

class ArgumentParser():

    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser(description='Reads path to input file')
        self._parser.add_argument('endpoints_file', type=str, help='Please enter the path to YAML file which contains your HTTP endpoints:')

    def parse(self):
        return self._parser.parse_args()

