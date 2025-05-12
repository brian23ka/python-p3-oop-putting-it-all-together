#!/usr/bin/env python3
# lib/book.py
class Book:
    def __init__(self, title="Unknown", page_count=0):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and value.strip():
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
