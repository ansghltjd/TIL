def solution(s):
    try:
        if len(s)==4 or len(s)==6:
            int(s)
            return True
        return False
    except:
        return False
    