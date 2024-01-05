"""
This main file reads input through console, parses contents, and then periodically (15s): makes API requests, and calculates availability. 
"""
from yamlparser import YamlParser
from reader import Reader
from yamlparser import YamlParser
from checkhealth import HealthChecker
import time
from logger import Logger, Levels

def main():
    logger = Logger(name=__name__, level=Levels.INFO)

    # Read data from file
    reader = Reader()
    lines = reader.read_file()
    
    # Parse contents of file into endpoint objects
    yaml_parser = YamlParser(lines=lines)
    yaml_parser.parse()
    endpoints = yaml_parser.endpoints

    # Config health checker
    checker = HealthChecker(endpoints=endpoints)

    # Periodically apply checker
    try:
        while True:
            logger.info('Health check initiated')
            checker.run()
            logger.info('Test cycle is completed.')
            time.sleep(15)  # Wait for 15 seconds before the next check
    except KeyboardInterrupt:
        print("Program stopped by the user.")


if __name__ == "__main__":
    main()
