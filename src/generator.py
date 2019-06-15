from json import loads
from random import choice, choices, randrange
from abstract.item import item

items_path = 'resources/items.json'
att_path = 'resources/attributes.json'

with open(items_path, 'r') as json_file:
    json_items = loads(json_file.read())

def _get_types():
    return choice(json_items['types'])

def get_item():
    type = _get_types()
    ATT_MIN = json_items['min-attributes']
    ATT_MAX = json_items['max-attributes']
    ATT_QTY = randrange(ATT_MIN, ATT_MAX)
    
    attributes_dict = json_items['attributes']
    key_list = choices(list(json_items['attributes']), k=ATT_QTY)

    attributes = {}
    for elem in key_list:
        min = attributes_dict[elem]['min']
        max = attributes_dict[elem]['max']
        att_val = randrange(min, max)
        attributes[elem] = att_val

    return str(item(type, attributes))
