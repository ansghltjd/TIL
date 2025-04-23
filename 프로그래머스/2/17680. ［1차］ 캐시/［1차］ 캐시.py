from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])

    if not cacheSize:
        return len(cities) * 5
    for i in cities:
        i = i.lower()
        if i.lower() in cache:
            answer+=1
            cache.remove(i)
            cache.append(i)
        else:
            answer+=5
            if len(cache)>=cacheSize:
                cache.popleft()
                cache.append(i)
            else:
                cache.append(i)
            
    return answer