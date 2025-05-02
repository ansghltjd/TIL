def to_sec(time):
    m,s = map(int,time.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = to_sec(video_len)
    pos_sec = to_sec(pos)
    op_start_sec = to_sec(op_start)
    op_end_sec = to_sec(op_end)
    
    for i in commands:
        if i == 'prev':
            pos_sec = max(0,pos_sec-10)
        elif i == 'next':
            if op_start_sec <= pos_sec <= op_end_sec:
                pos_sec = op_end_sec
            pos_sec = min(video_len_sec,pos_sec+10)
        
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
    m = pos_sec//60
    n = pos_sec%60
    return f"{m:02}:{n:02}"
                