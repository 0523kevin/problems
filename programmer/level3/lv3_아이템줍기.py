from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 전체 넓이, 간격이 겹치지 않도록 2배 해준다.
    field = [[-1] * 102 for i in range(102)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 태두리 부분 제외
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 태두리 부분 = 1
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    # 전체 도면의 크기 2배 해줬기 때문에 각각 2배 취함
    itemX *= 2
    itemY *= 2

    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # BFS 적용
    while q:
        x, y, cnt = q.popleft()
        if x == itemX and y == itemY:
            answer = field[x][y] // 2
            return answer
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < 102 and 0 <= ny and ny < 102 and field[nx][ny] == 1:
                field[nx][ny] = field[x][y] + 1
                q.append((nx, ny, cnt + 1))
                
