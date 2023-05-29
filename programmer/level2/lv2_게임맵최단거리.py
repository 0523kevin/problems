# 한칸씩 이동 할 때마다 1씩 더해주고 
# 마지막 도착지에서의 결과 값이 1이면 도착 하지 못한 것, 아니면 도착 한 결과를 나타냅니다
# 최단 경로 문제는 BFS 방식을 택합니다
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append([0,0])
    while queue:
        a, b = queue.popleft()
        da = [-1,1,0,0]
        db = [0,0,-1,1]
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or nb < 0 or na >= n or nb >= m:
                continue
            if maps[na][nb] == 0: 
                continue
            if maps[na][nb] == 1:
                maps[na][nb] = maps[a][b] + 1
                queue.append([na, nb])
            # 간출인 방법
            # if 0 <= na and 0 <= nb and na < n and nb < m and maps[na][nb] == 1:
            #     maps[na][nb] = maps[a][b] + 1
            #     queue.append([na, nb])
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]