def solution(n):
    f_0 = 0
    f_1 = 1
    num = 2
    while num >= 2 and num <= n:
        f_n = f_0 + f_1
        f_0 = f_1
        f_1 = f_n
        num += 1
    return f_n % 1234567