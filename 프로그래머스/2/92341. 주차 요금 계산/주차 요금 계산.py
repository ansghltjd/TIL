from collections import defaultdict
import math
def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    parking = dict()
    total_time = defaultdict(int)
    
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m
    
    for record in records:
        time_str, car_num, status = record.split()
        time = time_to_minutes(time_str)
        
        if status == 'IN':
            parking[car_num] = time
        elif status == 'OUT':
            in_time = parking.pop(car_num)
            total_time[car_num] += time - in_time
            
    for car_num, in_time in parking.items():
        total_time[car_num] += time_to_minutes('23:59') - in_time
        
    answer = []
    for car_num in sorted(total_time.keys()):
        time = total_time[car_num]
        if time <= basic_time:
            fee = basic_fee
        else:
            fee = basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee
        answer.append(fee)
    return answer