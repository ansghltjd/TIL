def solution(numbers): # XOR
    return [((i ^ (i+1)) >> 2) + i + 1 for i in numbers]
