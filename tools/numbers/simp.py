from dotenv import load_dotenv
import os


def add(a, b):
    load_dotenv('.env.development')
    """
    Name: Artiom
    Function Name: add
    Description: sum of two number and setting attribute for function in sumofdigits and ispal module comp
    :return sum of numbers
    """
    setattr(add, str(os.getenv('SIMP_ATTRIBUTE')), True)
    return a + b


def subtract(a, b):
    """
    Name: Artiom
    Function Name: subtract
    Description: subtract of two number and setting attribute for function in sumofdigits and ispal module comp
    :return subtract of numbers
    """
    setattr(subtract, str(os.getenv('SIMP_ATTRIBUTE')), True)
    return a - b
