def solution(id_list, report, k):
    user_report_dic = {}
    for user_id in id_list:
        user_report_dic[user_id] = [0]
    for i in range(len(report)):
        user_reporting, user_reported = report[i].split(" ")
        if user_reporting not in user_report_dic[user_reported]:
            user_report_dic[user_reported].append(user_reporting)
    answer = []
    for user_id in id_list:
        if len(user_report_dic[user_id]) - 1 >= k:
            for user_to_email in user_report_dic[user_id][1:]:
                user_report_dic[user_to_email][0] += 1
    for user_id in id_list:
        answer.append(user_report_dic[user_id][0])
        # print(user_report_dic[user_id])
    # print(user_report_dic)
    return answer
