def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(timelogs)):
        success = True

        for j in range(7):
            current_day = (startday + j - 1) % 7 + 1  # 1~7 요일 계산
            if current_day <= 5:  # 평일만 검사
                # 희망 시각 + 10 계산 (올바르게 시/분 처리)
                hour = schedules[i] // 100
                minute = schedules[i] % 100 + 10
                if minute >= 60:
                    hour += 1
                    minute -= 60
                deadline = hour * 100 + minute

                if timelogs[i][j] > deadline:
                    success = False
                    break

        if success:
            answer += 1

    return answer