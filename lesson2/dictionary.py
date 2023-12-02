# from pprint import pprint

# Define
full_names = {
    'ali': 'rn',
    'ronak': 'hazini',
    'hamed': 'taheri',
    'age': 12,
    'children': ['a', 'b', 'c'],
    'is_child': False,
}

# Retrieve
# print(full_names['hamed'])
# print(full_names.get('hamed2', 'TAHERI'))

# Iterate
# for i in full_names:
#     print(i)
# for k in full_names.keys():
#     print(k)
# for v in full_names.values():
#     print(v)
# for k, v in full_names.items():
#     print(k, v)


# Set
# print(full_names)
# full_names['soroush'] = 'ghasemi'
# print(full_names)
# full_names.update(
#     {'arash': 'moezzi', 'akbar': 'ahmadi'}
# )
# print(full_names)
# full_names |= {'mohammad': 'asadian'}
# print(full_names)
# new_full_names = full_names | {'mina': 'asadian'}
# print(new_full_names)

# Dict In Dict
person = {
    'user_1': {
        'name': 'Ali Rn',
        'age': 26,
    },
    'user_2': {
        'name': 'Kimia Fadaei',
        'age': 15
    }
}

# print(person)
# print(person['user_1'])

# Condition
# is_hamed_in_dict = 'hamed' in full_names
# print(is_hamed_in_dict)
#
# if 'hamed' in full_names:
#     print('ok')
#

# print(
#     person['user_1']['name'],
#     person.get('user_1')['name'],
#     person.get('user_1').get('name'),
# )
#
# print(
#     'age' in person['user_1']
# )

# print(dir(full_names))
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# print(person)
# person.clear()
# print(person)

# new_person_1 = person  # Dict, List
# new_person_2 = person.copy()
# print(new_person_1)
# print(new_person_2)
#
# new_person_2.clear()
# print(person)
# new_person_1.clear()
# print(person)

# print(full_names.items())

# print(full_names.keys())
# print(full_names.values())

# x = full_names.pop('hamed')
# print(x)
# print(full_names)

# print(full_names)
#
# full_names.update({'kimia': 'fadaei'})
# print(full_names)
#
# full_names['amin'] = 'aminian'
# print(full_names)
#
# new_full_names = full_names | {'shakila': 'ameri'}
# print(new_full_names)
