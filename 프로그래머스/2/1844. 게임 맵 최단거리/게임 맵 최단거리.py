from collections import deque
def solution(maps):
    m = len(maps) # height
    n = len(maps[0]) # width

    v = [[0] * n for _ in range(m)]
    q = deque()
    q.append((0, 0, 1)) # x, y, time
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    while q:
        x, y, t = q.popleft()
        if x == n-1 and y == m-1:
            return t

        for dx, dy in directions:
            if (
                (0 <= x+dx < n)
                and (0 <= y+dy < m)
                and maps[y+dy][x+dx] == 1
                and v[y+dy][x+dx] == 0
            ):
                v[y+dy][x+dx] = 1
                q.append((x+dx, y+dy, t+1))

    return -1
