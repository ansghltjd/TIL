def solution(dirs):
    visited = set()
    
    x, y = 0, 0
    
    mov ={'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    
    for i in dirs:
        dx, dy = mov[i]
        nx, ny = x+dx, y+dy
        
        if -5<=nx<=5 and -5<=ny<=5:
            path = sorted([(x,y),(nx,ny)])
            visited.add(tuple(path))
            x, y = nx, ny
    return len(visited)