def solution(brown, yellow):
    answer = []

    by_sum = brown + yellow

    for width in range(3, brown//2):
        if by_sum%width==0:
            for height in range(3, brown//2):
                if width*height==by_sum and width>=height and (width-2)*(height-2)==yellow:
                    answer = [width, height]
                    return answer