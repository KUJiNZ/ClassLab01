import ast
import os
import pytest
from dotenv import load_dotenv

from test_tools.log import Log
from tools.numbers import simp

# LOGGER
LOG = Log("__simp__ ", "simp_log.log")
logger = LOG.logger


@pytest.fixture()
def setup():
    # ENV FILE
    load_dotenv('.env.test')
    return setup


@pytest.mark.test_add
def test_add(setup):
    """
    Name: Artiom
    Function Name: test_add
    Description: Testing adding two numbers
    """
    try:
        num1 = int(os.getenv('NUM_1'))
        num2 = int(os.getenv('NUM_2'))
        x = simp.add(num1, num2)
        assert x == num1 + num2
        logger.info(
            f"{test_add.__doc__}\nActual: {x} Expected: {num1 + num2}\n")
    except Exception as e:
        logger.exception(f"{test_add.__doc__}{e}\n")
        raise


@pytest.mark.test_subtract
def test_subtract(setup):
    """
    Name: Artiom
    Function Name: test_subtract
    Description: Testing subtracting two numbers
    """
    try:
        num1 = ast.literal_eval(os.getenv('NUM_1'))
        num2 = ast.literal_eval(os.getenv('NUM_2'))
        x = simp.subtract(num1, num2)
        assert x == num1 - num2
        logger.info(
            f"{test_add.__doc__}\nActual: {x} Expected: {num1 - num2}\n")
    except Exception as e:
        logger.exception(f"{test_add.__doc__}{e}\n")
        raise
