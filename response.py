"""
This file describes the schema of a Response object which includes the status code, latency, and outcome (enum) - UP or DOWN.
An outcome is considered as UP if:
- status code is 2xx, and
- latency is less than 500ms (=.5s)
"""
from enum import Enum

class Outcome(Enum):
    UP = 1
    DOWN = 0

class Response():
    def __init__(self, status_code: int, latency: float):
        self.status_code = status_code
        self.latency = latency
        
        # 1 if conditions are met, otherwise it is 0
        # code is 2xx and latency < 500 ms = .5 s
        outcome = Outcome.UP if (200<=self.status_code<300) and (self.latency < .5) else Outcome.DOWN
        self.outcome = outcome

    def __repr__(self):
        return f"Response(status_code={self.status_code}, latency={self.latency}, outcome={self.outcome})"