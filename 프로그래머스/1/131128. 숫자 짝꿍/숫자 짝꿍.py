def solution(X, Y):
    answer =''
    for i in set(X):
        answer += min(X.count(i),Y.count(i)) * i
    if answer == '':
        return '-1'
    elif all(int(i)==0 for i in answer):
        return '0'
    return ''.join(sorted(answer,reverse=True))