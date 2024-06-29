def solution(s):
    answer=[]
    for i in s:
        if i=='(':
            answer.append(i)
        if i==')':
            if not answer or answer.pop() != '(':
                return False
    return len(answer)==0