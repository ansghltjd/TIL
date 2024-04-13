def solution(survey, choices):
    ##유형별 목록(같은 지표에서는 알파벳 순), score = 카테고리별 획득 점수
    category = ["R","T","C","F","J","M","A","N"]
    score = [0 for str in category]
    answer = ""

    ##choices에 따른 점수 부여
    for i in range(len(choices)):
        if 4<choices[i]<=7:
            score[category.index(survey[i][-1])] += choices[i]-4

        if choices[i] == 4:
            pass
        if 1<=choices[i]<4:
            score[category.index(survey[i][0])] += 4-choices[i]

    ##지표별 최종 유형 결정
    for i in range(len(score)//2):
        if score[2*i] >= score[2*i+1]:
            answer += category[2*i]
        else:
            answer += category[2*i+1]

    return answer