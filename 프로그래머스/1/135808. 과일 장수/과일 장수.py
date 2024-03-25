def solution(k, m, score):
    
    score.sort(reverse=True)
    cnt = len(score) // m
    answer = [score[m*i:m+m*i] for i in range(cnt)]
    res=[]
    for i in answer:
        res.append(min(i)*len(i))
        
    return sum(res)