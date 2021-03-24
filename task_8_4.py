def val_checker(x_num):
    def _val_checker(func):
        def wrapper(num):
            if x_num(num):
                print(func(num))
            else:
                raise ValueError(f"Неверное значение {num}")
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(11)
    b = calc_cube(10.5)
    c = calc_cube(-3)
except ValueError as err:
    print(err)
