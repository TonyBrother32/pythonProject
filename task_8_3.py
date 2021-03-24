from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        result_list = [num for num in args]
        result = [f'{func.__name__}({num}: {type(num)})' for num in result_list]
        print(*result, *func(*args), sep="\n")

    return wrapper


@type_logger
def calc_cube(*x):
    result_list = [num for num in x]
    return [el**3 for el in result_list]


a = calc_cube(5, 7, 9, 10.6)
