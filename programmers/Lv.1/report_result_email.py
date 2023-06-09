# Lv.1
# 신고 결과 받기
def solution(id_list, report, k):
    user_report_dic = {}
    # 각 유저의 이메일 개수 초기화하기
    for user_id in id_list:
        user_report_dic[user_id] = [0]
    # 각 유저를 신고한 유저 저장하기
    for i in range(len(report)):
        user_reporting, user_reported = report[i].split(" ")
        if user_reporting not in user_report_dic[user_reported]: # 중복 신고 방지
            user_report_dic[user_reported].append(user_reporting)
    # 각 유저가 받을 이메일 계산하기
    answer = []
    for user_id in id_list:
        if len(user_report_dic[user_id]) - 1 >= k:
            for user_to_email in user_report_dic[user_id][1:]:
                user_report_dic[user_to_email][0] += 1
    for user_id in id_list:
        answer.append(user_report_dic[user_id][0])
    return answer
