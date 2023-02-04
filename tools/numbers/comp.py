def sumofdigits(num):
    return sum(map(int, str(num)))


def ispal(num):
    return str(num) == str(num)[::-1]
