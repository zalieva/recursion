def factorial(number: int) -> int:
    if isinstance(number, int):
        if number == 0:
            return 1
        else:
            return number * factorial(number - 1)
    else:
        raise ValueError('not int')
