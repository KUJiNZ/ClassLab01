import os
from tools.numbers import simp


def sumofdigits(num):
    if hasattr(simp.add, str(os.getenv('SIMP_ATTRIBUTE'))) or hasattr(simp.subtract, str(os.getenv('SIMP_ATTRIBUTE'))):
        return sum(map(int, str(num)))
    raise Exception("You need to call a function from simp module first.")


def ispal(num):
    if hasattr(simp.add, str(os.getenv('SIMP_ATTRIBUTE'))) or hasattr(simp.subtract, str(os.getenv('SIMP_ATTRIBUTE'))):
        return str(num) == str(num)[::-1]
    raise Exception("You need to call a function from simp module first.")
