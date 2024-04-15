def solution(wallpaper):
    y=[]
    x=[]
    for y_idx,i in enumerate(wallpaper):
        for x_idx,j in enumerate(i):
            if j == '#':
                y.append(y_idx)
                x.append(x_idx)
    return [min(y),min(x),max(y)+1,max(x)+1]