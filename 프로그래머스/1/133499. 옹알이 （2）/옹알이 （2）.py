def solution(babbling):
    cnt=0
    for i in babbling :
        tmp = ''
        tmp2 = ''
        for j in i :
            tmp +=j
            if tmp == tmp2 :
                break
            if tmp in ('aya','ye','woo','ma'):
                tmp2=tmp
                tmp=''
        if tmp == '' :
            cnt+=1
    return cnt