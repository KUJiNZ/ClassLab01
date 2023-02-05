import os
from tools.numbers import simp


def sumofdigits(num):
    """
    Name: Artiom
    Function Name: sumofdigits
    Description: summing of number digits
    :return sum of digits
    """
    print(str(os.getenv('SIMP_ATTRIBUTE')))
    if hasattr(simp.add, str(os.getenv('SIMP_ATTRIBUTE_COMPARE'))) or hasattr(simp.subtract, str(os.getenv('SIMP_ATTRIBUTE_COMPARE'))):
        return sum(map(int, str(num)))
    raise Exception("You need to call a function from simp module first.")


def ispal(num):
    """
    Name: Artiom
    Function Name: ispal
    Description: checking if num is palindrome
    :return Bool
    """
    print(str(os.getenv('SIMP_ATTRIBUTE')))
    if hasattr(simp.add, str(os.getenv('SIMP_ATTRIBUTE_COMPARE'))) or hasattr(simp.subtract, str(os.getenv('SIMP_ATTRIBUTE_COMPARE'))):
        return str(num) == str(num)[::-1]
    raise Exception("You need to call a function from simp module first.")
