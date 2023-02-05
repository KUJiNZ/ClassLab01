from dotenv import load_dotenv
from test_tools.log import Log
from tools import col
import ast
import os
import pytest

# LOGGER
LOG = Log("__col__ ", "col_log.log")
logger = LOG.logger


@pytest.fixture()
def setup():
    # ENV FILE
    load_dotenv('.env.test')
    return setup


@pytest.mark.test_myzip
def test_myzip(setup):
    """
    Name: Artiom
    Function Name: test_myzip
    Description: Testing implementing zip function for 2 collections
    """
    try:
        item_1 = ast.literal_eval(os.getenv('ITEM_1'))
        item_2 = ast.literal_eval(os.getenv('ITEM_2'))
        x = col.myzip(item_1, item_2)
        assert type(x) is zip and not None
        logger.info(
            f"{test_myzip.__doc__}\nActual: {x} Expected: zip and not None\n")
    except Exception as e:
        logger.exception(f"{test_myzip.__doc__}{e}\n")
        raise
