def solution(id_list, report, k):
    report = set(report)
    report_cnt = {id: 0 for id in id_list} # 유저 별 신고 당한 횟수
    user_reports = {id: [] for id in id_list} # 내가 신고한 유저 리스트

    for r in report: # u : 신고한 사람 r_id : 신고당한 사람
        u, r_id = r.split()
        report_cnt[r_id] += 1
        user_reports[u].append(r_id)

        
    answer = []
    for user in id_list:
        mail_cnt = 0
        for reported in user_reports[user]:
            if report_cnt[reported] >= k:
                mail_cnt += 1
        answer.append(mail_cnt)
    
    return answer

    
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))