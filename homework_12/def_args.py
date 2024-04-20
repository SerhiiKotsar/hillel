"""
We have builtins function min(), max() but you can't use it
    1. Implement your own implementation of function max
    2. Implement your own min function
"""


def my_min(*args):
    min_value = args[0]
    for arg in args:
        if arg < min_value:
            min_value = arg
    return min_value


def my_max(*args):
    max_value = args[0]
    for arg in args:
        if arg > max_value:
            max_value = arg
    return max_value


if __name__ == '__main__':
    print('Min value is: ' + str(my_min(1, 0, -1)))
    print('Max value is: ' + str(my_max(1, 5, 15, 0, -1)))
