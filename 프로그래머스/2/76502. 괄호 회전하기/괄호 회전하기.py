def solution(s):
    result=0
    for i in range(len(s)):
        sub = s[i:len(s)] + s[:i]
        answer = []
        for j in sub:
            if not answer:
                answer.append(j)
                continue
            if ((answer[-1]=='[' and j==']') or 
                (answer[-1]=='(' and j==')') or 
                (answer[-1]=='{' and j=='}')):
                answer.pop()
            else:
                answer.append(j)
        result +=1 if not answer else 0
            
    return result