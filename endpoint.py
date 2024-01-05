"""
Defines the schema of an Endpoint object. 
Name, url, and domain are guaranteed to exist. Other params are optional. 
if `method` is not provided, the default is `GET`
"""

class Endpoint(): 
    def __init__(self, name="", url="", method="GET", headers=None, body=None) -> None:
        self.name: str = name
        self.url: str = url
        self.domain: str = ""

        self.method: str = method
        self.headers: dict = headers
        self.body: dict = body

    def __repr__(self):
        return f"Endpoint(name={self.name}, url={self.url}, domain={self.domain}, method={self.method}, headers={self.headers}, body={self.body})"
    