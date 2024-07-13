def solution(s):
    answer = []
    for i in s.split(' '):
        if i:
            if i[0].isdigit():
                answer.append(i.lower())
            else:
                answer.append(i[0].upper()+i[1:].lower())
        else :
            answer.append('')
    return ' '.join(answer)