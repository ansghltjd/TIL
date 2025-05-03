from collections import Counter
def solution(str1, str2):
    answer = 0
    n = 0
    
    a = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    b = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    counter_a = Counter(a)
    counter_b = Counter(b)
    intersection = counter_a & counter_b
    union = counter_a | counter_b   
    
    inter_len = sum(intersection.values())
    union_len = sum(union.values())

    if union_len == 0:
        return 65536
    return int((inter_len / union_len) * 65536)