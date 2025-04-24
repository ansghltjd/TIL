def solution(s):
    answer = []
    
    s = s.replace('{{','').replace('}}','').split('},{')
    s.sort(key=lambda x : len(x))
    a=[i.split(',') for i in s]
    for i in a:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer