def solution(lottos, win_nums):
    answer = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    cnt_max=0
    cnt_min=0
    for i in lottos:
        cnt_min+=win_nums.count(i)
    cnt_max=cnt_min + lottos.count(0)
    
    return [answer[cnt_max],answer[cnt_min]]