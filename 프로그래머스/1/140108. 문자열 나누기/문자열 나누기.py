def solution(s):
    answer = []
    res=''
    for i,j in enumerate(s):
        res+=j
        if res.count(res[0])==len(res)-res.count(res[0]):
            answer.append(res)
            res=''
    if len(res)>0:
        answer.append(res)
    return len(answer)