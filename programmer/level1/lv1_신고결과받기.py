# 간략화된 답
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reporter_dic = {x:0 for x in id_list}
    reported = []
    for i in set(report):
        reporter_dic[i.split()[1]] += 1
    for i in set(report):
        if reporter_dic[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1 
    return answer

    
#나의 답
from collections import Counter
def solution(id_list, report, k):
    answer = []
    reported = []
    reporter_reported = set(report)
    warn = []
    one_list = []
    for i in reporter_reported:
        one_list.append(tuple(i.split()))
        reported.append(i.split()[1])
    reported_cnt = Counter(reported)
    for i,v in reported_cnt.items():
        if v>=k: 
            warn.append(i)
    reporter = []
    for k,v in one_list:
        if v in warn:
            reporter.append(k)
    reporter_cnt = Counter(reporter)
    for i in id_list:
        answer.append(reporter_cnt[i])
    return answer