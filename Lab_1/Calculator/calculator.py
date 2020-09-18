def sum(m, n):
    sign = 1 if n > 0 else -1
    n = abs(n)
    while n != 0:
        m += sign
        n -= 1
    return m

def divide(m, n):
    if n == 0:
        raise ZeroDivisionError
    
    i = 0
    isNegative = m > 0 and n < 0 or m < 0 and n > 0
    m = abs(m)
    n = abs(n)

    while m - n >= 0:
        m -= n
        i += 1

    i = -i if isNegative else i

    return i