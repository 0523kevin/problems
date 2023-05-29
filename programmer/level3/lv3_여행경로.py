# 공항과 도착지를 파고드는 경로를 저장 하며 DFS 방식을 택합니다
# 출발지에 해당하는 도착지 정보를 딕셔너리에 저장합니다

from collections import defaultdict
def solution(tickets):
    dic = defaultdict(list)
    for aboard, depart in tickets:
        dic[aboard].append(depart)
        dic[aboard].sort()
    path = []
    start = ['ICN']
    while start:
        air = start[-1]
        if not dic[air]:
            start.append(dic[air].pop(0))
        else:
            path.append(start.pop())
    return path[::-1]
    
    
