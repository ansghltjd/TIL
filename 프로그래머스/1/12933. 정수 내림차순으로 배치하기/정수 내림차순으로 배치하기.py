def solution(n):
    answer = [int(i) for i in str(n)]
    answer.sort(reverse=True)
    return int(''.join(map(str,answer)))