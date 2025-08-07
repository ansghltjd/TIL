from collections import deque
def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    visited = set()
    
    while queue:
        num, count = queue.popleft()
        if num == y:
            return count
        if num > y or num in visited:
            continue
        visited.add(num)
        
        queue.append((num + n, count + 1))
        queue.append((num * 2, count + 1))
        queue.append((num * 3, count + 1))

    return -1