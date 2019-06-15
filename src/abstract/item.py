from .base import base


class item(base):
    def __init__(self, type, attributes, name=''):
        self.name = name
        self.type = type
        self.attributes = attributes
