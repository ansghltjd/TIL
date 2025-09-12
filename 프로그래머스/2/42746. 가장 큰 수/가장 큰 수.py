def solution(numbers):
    answer = sorted(map(str, numbers), key = lambda x:x*3, reverse=True)
    return ''.join(answer) if answer[0]!='0' else '0'