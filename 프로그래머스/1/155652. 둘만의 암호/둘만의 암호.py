def solution(s, skip, index):
    apl = sorted(set('abcdefghijklmnopqrstuvwxyz')-set(skip))
    apl_len = len(apl)
    answer = ''
    for i in s :
        answer+=apl[(apl.index(i)+index)%apl_len]
    return answer