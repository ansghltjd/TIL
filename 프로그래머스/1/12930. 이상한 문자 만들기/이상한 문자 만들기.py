def solution(s):
    answer = s.split(' ')
    
    for idx,val in enumerate(answer):
        a=''    
        for idx2,val2 in enumerate(val):
            if idx2%2==1:
                a+=val2.lower()
            elif idx2%2==0:
                a+=val2.upper()
        answer[idx]=a
        
    return ' '.join(answer)