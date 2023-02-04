import ast
import os
import pytest

from test_tools.log import Log
from tools.numbers import comp
from dotenv import load_dotenv

# LOGGER
LOG = Log("__comp__ ", "comp_log.log")
logger = LOG.logger

# ENV FILE
load_dotenv('.env.test')


@pytest.mark.test_sumofdigits
def test_sumofdigits():
    """
    Name: Artiom
    Function Name: test_sumofdigits
    Description: Testing sum of number digits
    """
    try:
        num = int(os.getenv('NUM'))
        x = comp.sumofdigits(num)
        assert x == sum(map(int, str(num))) and x is not None
        logger.info(
            f"{test_sumofdigits.__doc__}\nActual: {x} Expected: {sum(map(int, str(num)))} not None\n")
    except Exception as e:
        logger.exception(f"{test_sumofdigits.__doc__}{e}\n")
        raise


@pytest.mark.test_ispal
def test_ispal():
    """
    Name: Artiom
    Function Name: test_ispal
    Description: Testing checking if the number is palindrome
    """
    try:
        num = int(os.getenv('NUM_PAL'))
        print(num)
        x = comp.ispal(num)
        assert x is True
        logger.info(
            f"{test_ispal.__doc__}\nActual: {x} Expected: {True} not None\n")
    except Exception as e:
        logger.exception(f"{test_ispal.__doc__}{e}\n")
        raise
