import math
def solution(n):
    answer = 0
    for i in range(0, int(n//2)+1):
        one = n-(2*i)
        two = i
        m =math.comb(one+two,two)
        answer += m
    return answer % 1234567