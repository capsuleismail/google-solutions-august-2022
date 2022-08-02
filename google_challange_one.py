def solution(a):
    res = []
    while a > 0:
        side = int(a**0.5)
        big = side**2
        a -= big
        res.append(big)
    return print(res)


solution(12)
