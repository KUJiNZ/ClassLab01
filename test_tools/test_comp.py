import ast
import os
import pytest

from test_tools.log import Log
from tools.numbers import comp
from tools.numbers import simp
from dotenv import load_dotenv


# LOGGER
LOG = Log("__comp__ ", "comp_log.log")
logger = LOG.logger


@pytest.fixture()
def setup():
    # ENV FILE
    load_dotenv('.env.test')
    num1 = ast.literal_eval(os.getenv('NUM_1'))
    num2 = ast.literal_eval(os.getenv('NUM_2'))
    add_call = simp.add(num1, num2)  # need to call to avoid raise exception that rules tells
    return setup


@pytest.mark.test_sumofdigits
def test_sumofdigits(setup):
    """
    Name: Artiom
    Function Name: test_sumofdigits
    Description: Testing sum of number digits
    """
    try:
        num = int(os.getenv('NUM'))
        x2 = comp.sumofdigits(num)
        assert x2 == sum(map(int, str(num))) and x2 is not None
        logger.info(
            f"{test_sumofdigits.__doc__}\nActual: {x2} Expected: {sum(map(int, str(num)))} not None\n")
    except Exception as e:
        logger.exception(f"{test_sumofdigits.__doc__}{e}\n")
        raise


@pytest.mark.test_ispal
def test_ispal(setup):
    """
    Name: Artiom
    Function Name: test_ispal
    Description: Testing checking if the number is palindrome
    """
    try:
        num = int(os.getenv('NUM_PAL'))
        x = comp.ispal(num)
        assert x is True
        logger.info(
            f"{test_ispal.__doc__}\nActual: {x} Expected: {True} not None\n")
    except Exception as e:
        logger.exception(f"{test_ispal.__doc__}{e}\n")
        raise
