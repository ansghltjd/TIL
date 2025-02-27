def solution(k, tangerine):
    answer = 0
    dic= {}
    for i in tangerine:
        if dic.get(i)==None:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in sorted(dic.values(),reverse=True):
        k-=i
        answer+=1
        if k<=0:
            return answer
            
                    