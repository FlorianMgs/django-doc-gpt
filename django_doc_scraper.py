import requests

from functools import lru_cache
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from bs4 import BeautifulSoup


class DjangoDocScraper:
    ROOT_URL = "https://docs.djangoproject.com/en/4.2/contents/"

    def __init__(self) -> None:
        self.root_url_parts = urlparse(self.ROOT_URL)

    def get_urls(self) -> List[str]:
        root_response = requests.get(self.ROOT_URL)
        root_html = root_response.content.decode("utf-8")
        soup = BeautifulSoup(root_html, "html.parser")
        root_links = soup.find_all("a", attrs={"class": "reference internal"})
        return [
            self.root_url_parts.path + root_link.get("href") for root_link in root_links
        ]

    def clean_urls(self, url_list: List):
        result = set()
        for url in url_list:
            path = str(Path(url).resolve())
            path = urlparse(path).path
            cleaned_url = (
                f"{self.root_url_parts.scheme}://{self.root_url_parts.netloc}{path}"
            )
            if not cleaned_url.endswith("/"):
                cleaned_url += "/"
            result.add(cleaned_url)

        return list(result)

    @lru_cache(maxsize=None)
    def urls(self) -> List[str]:
        return self.clean_urls(self.get_urls())
