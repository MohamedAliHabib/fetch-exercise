"""
Utility helper functions.

- extract_domain: parses a string url and extract the domain. Example: https://fetch.com/careers domain is fetch.com
"""

from urllib.parse import urlparse

def extract_domain(url: str):
    """Extracts domain URL from endpoint URL"""
    parsed_url = urlparse(url)
    return parsed_url.netloc