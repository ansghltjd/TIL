def solution(files):
    answer = []
    
    for idx, file in enumerate(files):
        num_start = 0
        # 1) 숫자가 시작하는 위치 찾기
        while not file[num_start].isdigit():
            num_start += 1
        num_end = num_start
        # 2) 숫자 부분 (연속된 숫자, 최대 5자리)
        while num_end<len(file) and file[num_end].isdigit() :
            num_end += 1
        number = file[num_start:num_end]
        head = file[:num_start].lower()
        
        answer.append((head, int(number), idx, file))
    # HEAD(소문자) -> NUMBER(int) -> original index(안정성 확보)
    answer.sort(key = lambda x : (x[0], x[1], x[2]))

    return [i[3] for i in answer]