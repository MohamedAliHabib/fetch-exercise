"""
This file processes the list of strings (lines from YAML file), and create endpoint objects matching the schema (Endpoint).
"""
from typing import List
from endpoint import Endpoint
import ast
import json
from utils import extract_domain
from logger import Logger, Levels

logger = Logger(name=__name__, level=Levels.INFO)

class YamlParser():

    NON_HEADER_TYPES = ['method', 'name', 'url', 'body']

    def __init__(self, lines: List[str]) -> None:
        self._lines: List[str] = lines
        self.endpoints: List[Endpoint] = []

    def parse(self):
        """Parses the text lines to extract endpoints."""
        endpoint = None
        processing_headers = False
        
        for line in self._lines:
            line = line.strip()

            # new endpoints start with '-' according to schema                        
            if line.startswith('-'):
                if endpoint:                 
                    self.endpoints.append(endpoint)
                endpoint = Endpoint()

            if 'headers' in line:
                # process the headers in the next few lines
                processing_headers = True 
                continue

            # parse current line
            if ':' in line and endpoint:
                key, value = self._parse_line(line)
                
                if key in self.NON_HEADER_TYPES:
                    if processing_headers: 
                        processing_headers = False 
                    # process non-headers (e.g., method, url, name, etc.)
                    self._process_non_header_types(endpoint=endpoint, key=key, value=value)

                elif processing_headers:
                    self._process_headers(endpoint, key, value)

        if endpoint: self.endpoints.append(endpoint)

        logger.info(f'Finished parsing. # of endpoints: {len(self.endpoints)}')
        for e in self.endpoints:
            logger.info(e)
        
    def _parse_line(self, line: str):
        """ Parses a line and returns the key-value pair. """
        if line.startswith('-'):
            line = line[2:]
        key, value = line.split(':', 1)
        key = key.strip().lower()
        value = value.strip()
        return key, value

    def _process_non_header_types(self, endpoint: Endpoint, key: str, value: str):
        """Processes non-header types in the YAML."""
        if key == 'name': endpoint.name = value
        elif key == 'method': endpoint.method = value
        elif key == 'url': 
            endpoint.url = value
            endpoint.domain = extract_domain(value)
        elif key == 'body': 
            body = ast.literal_eval(value)
            endpoint.body = json.loads(body)

    def _process_headers(self, endpoint: Endpoint, key: str, value: str):
        """Processes header types in the YAML."""
        if not endpoint.headers:
            endpoint.headers = {}
        endpoint.headers[key] = value            

                

