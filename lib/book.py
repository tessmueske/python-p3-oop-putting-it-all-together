#!/usr/bin/env python3

class Book:
    def __init__(self, title = "And Then There Were None", page_count = 272):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        """The title property"""
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """"page_count must be an integer"""
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Prints a message indicating the page is being turned"""
        print("Flipping the page...wow, you read fast!")