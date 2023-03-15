#!/usr/bin/env python3

class Book:
    _page_count = 0
    def __init__(self, title):
        self.title = title
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    def set_page_count(self, count):
        if (type(count) in (int, float)):
            self._page_count = count
        else:
            print("page_count must be an integer")
    def get_page_count(self):
        return self._page_count

    page_count = property(get_page_count, set_page_count)

