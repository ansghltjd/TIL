def solution(clothes):
    answer = 1
    a = {}
    for i in clothes:
        if a.get(i[1]):
            a[i[1]]+=1
        else:
            a[i[1]]=1
    for count in a.values():
        answer *= count+1
    return answer -1