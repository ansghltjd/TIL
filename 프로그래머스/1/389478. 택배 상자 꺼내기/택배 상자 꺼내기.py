def solution(n, w, num):

    box = list()
    for i in range(1,n+1,w):
        row = list(range(i,min(i+w,n+1)))
        
        if len(box) % 2 == 1:
            row.reverse()
        box.append(row)
        
    cnt = 0
    idx = None
    
    for i in range(len(box)):
        if num in box[i]:
            idx = box[i].index(num)
            cnt+=1
        elif idx is not None:
            if i % 2 == 0 and idx < len(box[i]) :
                cnt+=1
            elif i % 2 == 1 and len(box[i-1])-idx<=len(box[i]):
                cnt+=1
        
    return cnt