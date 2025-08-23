def solution(numbers):
    answer = sorted(map(str,numbers), key = lambda x : x*3, reverse =True)
    answer = ''.join(answer)
    return '0' if answer[0] == '0' else answer