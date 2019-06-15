from json import loads
from os.path import join
from random import choice, choices, randrange
from abstract.item import item

items_path = join('src','resources','items.json')

with open(items_path, 'r') as json_file:
    json_items = loads(json_file.read())

def _get_types():
    _type = choice(json_items['types'])
    _subtype = choice(json_items['subtypes'][_type])
    return _type, _subtype

def _get_name(type, subtype, attributes):
    if type == 'weapon':
        pass
    elif type == 'item':
        pass
    elif type == 'equipment':
        pass

    return '{0} of {1}'.format(subtype, choice(list(attributes)))

def get_item():
    type, subtype = _get_types()
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


    name = _get_name(type, subtype, attributes)
    return str(item(type, attributes, name=name))
