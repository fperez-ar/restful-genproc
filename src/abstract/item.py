from .base import base


class item(base):
    def __init__(self, name, attributes):
        self.type = name
        self.attributes = attributes
