"""
This file takes an Endpoint object, and performs the following:
- Performs the corresponding HTTP request and processes the response.
- Returns a Response object which includes the status code, latency, and outcome - 'UP' or 'DOWN'.
"""
from endpoint import Endpoint
import requests
from response import Response
from logger import Logger, Levels

logger = Logger(name=__name__, level=Levels.INFO)

class Caller():

    def __init__(self, endpoint: Endpoint) -> None:
        self.endpoint = endpoint
        
        self._functions = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete,
            'PATCH': requests.patch,
            'HEAD': requests.head,
        }

    def call(self) -> Response:
        try:
            headers = None if not self.endpoint.headers else self.endpoint.headers
            body = None if not self.endpoint.body else self.endpoint.body
            url = self.endpoint.url
            
            func = self._functions[self.endpoint.method]
            response = func(url, headers=headers, json=body)
        
            code = response.status_code
            latency = response.elapsed.total_seconds()
            
            result = Response(status_code=code, latency=latency)
            logger.info(f'Called: {self.endpoint}, Received: {result}')
            return result
            
        except requests.RequestException as e:
            logger.error(f"error: {e}")
            return {"error": str(e)}
        
        