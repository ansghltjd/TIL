def solution(elements):
    # 원형 수열을 두 배로 확장
    extended_elements = elements + elements
    unique_sums = set()
    
    # 부분 수열 합을 계산
    for length in range(1, len(elements) + 1):  # 부분 수열의 길이는 1부터 len(elements)까지
        for start in range(len(elements)):  # 부분 수열의 시작 인덱스
            subarray_sum = sum(extended_elements[start:start + length])
            unique_sums.add(subarray_sum)
    
    return len(unique_sums)
