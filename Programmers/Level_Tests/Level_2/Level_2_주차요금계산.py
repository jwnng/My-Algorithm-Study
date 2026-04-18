"""
문제: 주차 요금 계산 (구현/해시)
난이도: Level 2

[오늘의 삽질 포인트]
1. 누적 시간 유실 오류: 
   - 처음에 '입-출차' 한 세트마다 바로 요금을 계산하거나 리스트에 담으려다 보니, 
     한 차량이 여러 번 입출차했을 때 총 주차 시간이 합산되지 않고 덮어씌워지는 문제가 발생함.
   - 해결: '요금 계산' 전에 먼저 '차량별 총 주차 시간'을 완전히 합산하는 해시 테이블이 별도로 필요함을 깨달음.

2. 23:59 강제 출차 처리:
   - 출차 기록이 없는 차량을 'pk_fee_cal' 리스트에서 찾아서 더하려다 보니 로직이 복잡해짐.
   - 해결: 아예 '누적 시간 해시'를 먼저 완성한 뒤, 마지막에 일괄 요금 계산을 하는 것이 훨씬 깔끔함.

[핵심 로직]
- 입차 시 Dictionary에 입차 시간 저장.
- 출차 시 (현재 시간 - 입차 시간)을 계산하여 '누적 시간 전용 딕셔너리'에 더해줌.
- 모든 기록 확인 후 아직 Dictionary에 남은(출차 안 한) 차량은 23:59 기준으로 최종 합산.
- 합산된 누적 시간을 기준으로 요금 공식 적용 및 차량 번호순 정렬.
"""

import math
from collections import defaultdict
def pk_time_cal(in_time,out_time):
    in_h, in_m = map(int, in_time.split(':'))
    out_h, out_m = map(int, out_time.split(':'))
    return (out_h * 60 + out_m) - (in_h * 60 + in_m)
    
def solution(fees, records):
    answer = []
    pk_lot = defaultdict(list)
    pk_fee_cal = []
    for r in records:
        time, number, status = r.split()
        
        if status == 'IN': # 입차 시
            pk_lot[number] = [time,status]
        elif status == 'OUT': # 출차 시 
            if number in pk_lot.keys():
                in_time = pk_lot[number][0]
                pk_lot[number] = [time,status] # 해시에 시간, 상태 최신화
                pk_time = pk_time_cal(in_time,time)
                
                pk_fee_cal.append([number,pk_time])
    for number,v in pk_lot.items():
        if v[1] == 'IN':
            pk_time = pk_time_cal(v[0],'23:59')
        
            for i in range(len(pk_fee_cal)):
                if number == pk_fee_cal[i][0]:
                    pk_fee_cal[i][1] += pk_time
    
    for item in pk_fee_cal:
        if item[1] <= int(fees[0]):
                answer.append([item[0],fees[1]])
        else:
            pk_fee = fees[1] + (((item[1]-fees[0])//fees[2]) * fees[3])
            answer.append([item[0],pk_fee])

    answer.sort(key=lambda x: x[0],reverse=True)
    return answer[1]

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))