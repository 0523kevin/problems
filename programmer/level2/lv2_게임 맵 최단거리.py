
from collections import deque
def solution(maps):
    row, column = len(maps), len(maps[0])
    queue = deque([(0,0)])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + directions[i][0]
            nb = b + directions[i][1]
            if 0 <= na and na < row and 0 <= nb and nb < column and maps[na][nb] == 1:
                maps[na][nb] = maps[a][b] + 1
                queue.append((na,nb))
    return maps[-1][-1] if maps[-1][-1] > 1 else -1





            
            