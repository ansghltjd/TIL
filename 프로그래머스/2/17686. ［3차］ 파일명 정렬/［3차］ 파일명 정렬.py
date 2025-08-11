def solution(files):
    parsed = []
    for idx, f in enumerate(files):
        n = len(f)
        i = 0
        # 1) 숫자가 시작하는 위치 찾기
        while i < n and not f[i].isdigit():
            i += 1
        head = f[:i]
        # 2) 숫자 부분 (연속된 숫자, 최대 5자리)
        j = i
        while j < n and f[j].isdigit() and (j - i) < 5:
            j += 1
        number = f[i:j]
        # tail = f[j:]  # 정렬 키에는 필요 없음 (원본 반환만)
        # 정렬용 키: (head 소문자, 숫자 정수값, 원래 인덱스)
        parsed.append((head.lower(), int(number), idx, f))

    # HEAD(소문자) -> NUMBER(int) -> original index(안정성 확보)
    parsed.sort(key=lambda x: (x[0], x[1], x[2]))

    return [t[3] for t in parsed]