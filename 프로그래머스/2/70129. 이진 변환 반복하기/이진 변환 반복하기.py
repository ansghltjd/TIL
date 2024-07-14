def solution(s):
    answer = []
    zero = 0
    cnt= 0
    while s != '1':
        zero += s.count('0')
        s = s.replace('0','')
        s = format(len(s), 'b')
        cnt+=1
    return [cnt,zero]