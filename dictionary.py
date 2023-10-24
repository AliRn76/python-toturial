# from pprint import pprint

full_names = {
    'ali': 'rn',
    'ronak': 'hazini',
    'hamed': 'taheri',
    'age': 12,
    'children': ['a', 'b', 'c'],
    'is_child': False,
}

print(full_names['hamed'])
for i in full_names['children']:
    print(i)
full_names['soroush'] = 'ghasemi'
print(full_names)


# person = {
#     'user_1': {
#         'name': 'Ali Rn',
#         'age': 26,
#     },
#     'user_2': {
#         'name': 'Kimia Fadaei',
#         'age': 15
#     }
# }


# print(full_names['ali'])
# print(full_names['age'])
# print(full_names.get('kimia'))
#
#
# is_hamed_in_dict = 'hamed' in full_names
#
# if 'hamed' in full_names:
#     print('ok')


# print(
#     person['user_1']['name'],
#     person.get('user_1')['name'],
#     person.get('user_1').get('name'),
# )
#
# print(
#     'age' in person['user_1']
# )

# print(dir(person))
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# person.clear()
# print(person)

# new_person = person.copy()
# print(new_person)


# print(full_names.items())

# print(full_names.keys())
# print(full_names.values())

# full_names.pop('hamed')
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
