class base():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.attributes = {}

    def __str__(self):
        dict_obj = {}
        dict_obj['name'] = self.name
        dict_obj['type'] = self.type
        dict_obj['attributes'] = self.attributes

        return str(dict_obj)
