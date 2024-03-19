def solution(name, yearning, photo):
    answer = []
    dic = {i:j for i,j in zip(name,yearning)}
    for i in photo :
        a=0
        for j in i:
            if j in name :
                a+=dic[j]
        answer.append(a)
    return answer