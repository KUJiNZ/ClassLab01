import ast
import os

from dotenv import load_dotenv


def add(a, b):
    """
    Name: Artiom
    Function Name: add
    Description: sum of two number and setting attribute for function in sumofdigits and ispal module comp
    :return sum of numbers
    """
    load_dotenv('D:/PythonRepos/ClassLab1/tools/.env.development')
    setattr(add, str(os.getenv('SIMP_ATTRIBUTE')), True)
    return a + b


def subtract(a, b):
    """
    Name: Artiom
    Function Name: subtract
    Description: subtract of two number and setting attribute for function in sumofdigits and ispal module comp
    :return subtract of numbers
    """
    load_dotenv('D:/PythonRepos/ClassLab1/tools/.env.development')
    setattr(subtract, str(os.getenv('SIMP_ATTRIBUTE')), True)
    return a - b
