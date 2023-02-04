import pytest

import tools.numbers.simp as simp
import tools.numbers.comp as comp
import tools.col as col

if __name__ == '__main__':
    # print(simp.add(1, 2))
    # print(simp.subtract(5, 3))
    # print(comp.sumofdigits(234))
    # print(comp.ispal(1221))
    # print(list(col.myzip([1, 2, 3], [4, 5, 6])))
    # print(type(col.myzip([1, 2, 3], [4, 5, 6])))

    pytest.main(['D:/PythonRepos/ClassLab1/test_tools/test_simp.py','D:/PythonRepos/ClassLab1/test_tools/test_comp.py','D:/PythonRepos/ClassLab1/test_tools/test_col.py'])
