def solution(arr):
    n = len(arr)
    def cut(x,y,size):
        start = arr[x][y]
        check = True
        for i in range(x,x+size):
            for j in range(y,y+size):
                if arr[i][j] != start:
                    check = False
                    break
            if not check:
                break
        if check:
            return (1,0) if start == 0 else (0,1)
        
        half = size // 2
        a0, a1 = cut(x, y, half)
        b0, b1 = cut(x, y+half, half)
        c0, c1 = cut(x+half, y, half)
        d0, d1 = cut(x+half, y+half, half)
        return (a0+b0+c0+d0, a1+b1+c1+d1)
    zero, one = cut(0,0,n)
    return [zero, one]