def solution(n):
    answer = n
    while 1 :
        answer += 1
        if bin(answer).count('1') == bin(n).count('1'):
            break
    return answer