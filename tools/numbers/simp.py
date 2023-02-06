import os


def add(a, b):
    """
    Name: Artiom
    Function Name: add
    Description: sum of two number and setting attribute for function in sumofdigits and ispal module comp
    :return sum of numbers
    """
    try:
        if type(a) is int or float and type(b) is int or float:
            setattr(add, str(os.getenv('SIMP_ATTRIBUTE')), True)
            return a + b
    except Exception as e:
        raise e


def subtract(a, b):
    """
    Name: Artiom
    Function Name: subtract
    Description: subtract of two number and setting attribute for function in sumofdigits and ispal module comp
    :return subtract of numbers
    """
    try:
        if type(a) is int or float and type(b) is int or float:
            setattr(subtract, str(os.getenv('SIMP_ATTRIBUTE')), True)
            return a - b
    except Exception as e:
        raise e
