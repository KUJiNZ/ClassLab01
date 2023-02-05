from dotenv import load_dotenv

import tools.numbers.simp as simp
import tools.numbers.comp as comp
import tools.col as col


if __name__ == '__main__':
    load_dotenv('.env.development')
    simp.add(1, 2)
    simp.subtract(5, 3)
    print(comp.sumofdigits(234))
    print(comp.ispal(1221))
    print(list(col.myzip([1, 2, 3], [4, 5, 6])))
    print(type(col.myzip([1, 2, 3], [4, 5, 6])))



