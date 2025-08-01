import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville,first+second*2)
        answer+=1

    return answer if scoville[0] >= K else -1
