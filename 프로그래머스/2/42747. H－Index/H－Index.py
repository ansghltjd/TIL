def solution(citations):
    result = 0
    citations.sort(reverse=True)
    for idx, i in enumerate(citations, start=1):
        print(idx,i)
        result = max(result, min(idx, i))

    return result