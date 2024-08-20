class Invalidnumber(Exception):

    ...


def check(a, b):
    if a <= 0 or b <= 0:
        raise Invalidnumber()
    return a + b


a = int(input("Enter a number :"))
b = int(input("Enter a number :"))


try:
    print(check(a, b))

except Invalidnumber:
    print('Number Cannot be less then zero')
