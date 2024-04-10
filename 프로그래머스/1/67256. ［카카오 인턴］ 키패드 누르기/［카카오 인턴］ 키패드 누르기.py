def solution(numbers, hand):
    answer = ''
    xy={
        1:[0,1],2:[0,2],3:[0,3],
        4:[1,1],5:[1,2],6:[1,3],
        7:[2,1],8:[2,2],9:[2,3],
        '*':[3,1],0:[3,2],'#':[3,3]
    }
    left=xy['*']
    right=xy['#']
    for i in numbers :
        start_xy=xy[i]
        if i in (1,4,7):
            answer+='L'
            left=xy[i]
        elif i in (3,6,9):
            answer+='R'
            right=xy[i]
        else:
            le=abs(start_xy[0]-left[0]) + abs(start_xy[1]-left[1])
            ri=abs(start_xy[0]-right[0]) + abs(start_xy[1]-right[1])
            if le > ri :
                right=xy[i]
                answer+='R'
            elif ri > le :
                left=xy[i]
                answer+='L'
            else:
                if hand=='right' :
                    right=xy[i]
                    answer+='R'
                else:
                    left=xy[i]
                    answer+='L'
    return answer