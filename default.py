import numbers


def greet_multiple(*names):
    print(names)
    for name in names:
        print(f"Hello {name}")
def addition(*numbers):
    s=0
    for number in numbers:
        s+=number
    return s
def multiply(*number):
    num=1
    for x in number:
        num*=x
    return num

        