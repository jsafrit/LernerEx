from collections import namedtuple


def myrange2(first, second=None, third=1):
    result = []
    if second is None:
        second = first
        first = 0
    while first < second:
        result.append(first)
        first += third
    return result


def myrange3(first, second=None, third=1):
    if second is None:
        second = first
        first = 0
    while first < second:
        yield first
        first += third
    return


if __name__ == '__main__':
    for x in myrange2(10, 30, 3):
        print(x)
    print()
    for x in myrange3(10, 30, 3):
        print(x)

    print(myrange2(5, 15, 2))
    print(myrange3(5, 15, 2))