def solution(s):
    a={}
    answer=[]
    for i,j in enumerate(s):
        if j not in a :
            answer.append(-1)
            a[j]=i
        elif j in a :
            answer.append(i-a[j])
            a[j]=i
        
    return answer