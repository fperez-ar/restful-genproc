class base():
    def __init__(self):
        self.type = ''
        self.attributes = {}

    def __str__(self):
        dict_obj = {}
        dict_obj['type'] = self.type
        dict_obj['attributes'] = self.attributes

        return str(dict_obj)
