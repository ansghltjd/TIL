from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    answer = 0
    total_weight = 0
    
    while bridge:
        total_weight -= bridge.popleft()
        if trucks:
            if trucks and total_weight + trucks[0] <= weight :
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)
        answer+=1
            
    return answer
