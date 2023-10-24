# For, While


# while True:
#     x = int(input())
#     if x == 7:
#         print('You won')
#         break
#
#     else:
#         print('try again')
# print('Game is finished')

# x = int(input())
# while x != 7:
#     print('try again')
#     x = int(input())
#
# print('You won')


names = {
    ('ali', 'rn'),
    ('kimia', 'fadaei'),
    ('ronak', 'hazini'),
    ('hamed', 'taheri'),
    ('shakila', 'ameri'),
    ('bahar', 'iri'),
}

for name in names:
    print(name[0] + ' ' + name[1])
