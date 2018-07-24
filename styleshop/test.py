#!/usr/bin/env python
my_dict = {
    'data': {
        'item1': {'first': 1, 'second': 2},
        'item2': {'first': 3, 'second': 4}
    }
}

for _, item in my_dict.items():
    for name, i in item.items():
        print('\n', i)
