def solution(id_list, report, k):
    user_report_dic = {}
    for user_id in id_list:
        user_report_dic[user_id] = [0]
    for i in range(len(report)):
        user_reporting, user_reported = report[i].split(" ")
        user_report_dic[user_reported].append(user_reporting)
#     for user_id in id_list:
        
    answer = []
    return answer
