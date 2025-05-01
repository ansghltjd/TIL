def solution(mats, park):
    n = len(park)
    m = len(park[0])
    
    for size in sorted(mats,reverse=True):
        for row_start in range(n-size+1):
            for col_start in range(m-size+1):
                place = True
                for x in range(row_start,row_start+size):
                    for y in range(col_start,col_start+size):
                        if park[x][y]!='-1':
                            place=False
                            break
                    if not place:
                        break
                if place:
                    return size
    return -1