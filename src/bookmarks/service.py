from dataclasses import dataclass

@dataclass
class Bookmark:
    url: str
    title: str
    tags: list[str]

class BookmarkService:
    def __init__(self):
        self.bookmarks: list[Bookmark] = []

    def add(self, url: str, title: str, tags: list[str]) -> Bookmark:
        bookmark = Bookmark(url, title, tags)
        self.bookmarks.append(bookmark)
        return bookmark

    def list_all(self) -> list[Bookmark]:
        return self.bookmarks
