

# try:
#     number = int('1')
#     print(number)
# except:
#     print('error')


# try:
#     number = int('2')
#     print(number)
#
#     number2 = number / 0
#     print(number2)
#
# except ValueError:
#     print('value error')
# except ZeroDivisionError:
#     print('zero error')


# try:
#     number = int('2')
#     print(number)
#
#     number2 = number / 0
#     print(number2)
#
# except (ValueError, ZeroDivisionError):
#     print('error')

# try:
#     number = int('2')
#     print(number)
#
#     number2 = number / 0
#     print(number2)
#
# except (ValueError, ZeroDivisionError):
#     print('error')
#
# finally:
#     print('Finished')


def exception():
    return 1 / 0


try:
    exception()
    print('Try Shod')

except (ValueError, ZeroDivisionError) as e:
    print(e)
    print('Exception')

else:
    print('Ok')

finally:
    print('Finished')

