from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  
    trucks = deque(truck_weights)        
    
    total_weight = 0                     
    answer = 0
    
    while bridge:
        answer += 1
        total_weight -= bridge.popleft()  

        if trucks:  
            if total_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  
    return answer
