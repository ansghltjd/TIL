def solution(keymap, targets):
    res=[]    
    for x in targets:        
        num=0
        for j in x :  
            answer = []
            for k in range(len(keymap)):                
                try:
                    answer.append(keymap[k].index(j)+1)
                except:
                    pass
            if len(answer) == 0:
                res.append(-1)
                num=0
                break
            else:
                num+=min(answer)
        if num != 0:
            res.append(num)
    return res