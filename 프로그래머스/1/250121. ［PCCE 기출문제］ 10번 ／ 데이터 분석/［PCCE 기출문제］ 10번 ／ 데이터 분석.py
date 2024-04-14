def solution(data, ext, val_ext, sort_by):
    
    a={
        'code':0,
        'date':1,
        'maximum':2,
        'remain':3
    }
    answer = [i for i in data if i[a[ext]] < val_ext]
    return sorted(answer,key= lambda x : x[a[sort_by]])