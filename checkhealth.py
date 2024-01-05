"""
This file takes a list of Endpoint objects, and performs the following: 
- Makes HTTP endpoint calls and records responses per domain.
- Calculates availibillity over the life of the program of each domain and prints results to console.
    - Availability percentage is defined as: 100 * (number of HTTP requests that had an outcome of UP / number of HTTP requests)
    - prints are as follows:
      fetch.com has 33% availability percentage
"""
from endpoint import Endpoint
from caller import Caller
from collections import defaultdict
from response import Response, Outcome
from typing import List
from logger import Logger, Levels

logger = Logger(name=__name__, level=Levels.INFO)

class HealthChecker():
    def __init__(self, endpoints) -> None:
        self.endpoints: List[Endpoint] = endpoints
        self.responses: List[Response] = defaultdict(list)

    def run(self):
        for e in self.endpoints:
            c = Caller(endpoint=e)
            response: Response = c.call()
            self.responses[e.domain].append(response)
        
        self._check_availability()
        
    def _check_availability(self):
        """Calculated & prints to console availability per domain."""
        for domain in self.responses:
            responses = self.responses[domain]

            # no. of up / total requests
            up_count = sum([1 for r in responses if r.outcome == Outcome.UP])
            total = len(self.responses[domain])

            availability = round((up_count / total)*100)
            
            logger.info(f'{domain} had {up_count} out of {total} as UP')
            print(f'{domain} has {availability}% availability percentage')
