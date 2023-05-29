# words의 단어들을 하나씩 꺼내서 queue 에 저장된 바뀐 단어와 비교합니다
# begin 단어를 시작으로 하여 queue에 저장된 단어를 꺼내서 비교하고 조건을 만족 하면 바뀜 처리 해줍니다 
# BFS 방법을 택합니다
# 딕셔너리와 단어 자체를 활용
from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    visited = {k:0 for k in words}
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            answer = cnt
        for i in words:
            dif_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != i[j]:
                        dif_cnt += 1
                if dif_cnt == 1:
                    queue.append([i, cnt + 1])
                    visited[i] += 1
    return answer

# 인덱스를 활용
# from collections import deque
# def solution(begin, target, words):
#     answer = 0
#     visited = [0 for i in range(len(words))]
#     queue = deque()
#     queue.append([begin, 0])
#     while queue:
#         word, cnt = queue.popleft()
#         if word == target:
#             answer = cnt
#             break
#         for i in range(len(words)):
#             change_cnt = 0
#             if not visited[i]:
#                 for j in range(len(word)):
#                     if word[j] != words[i][j]:
#                         change_cnt += 1
#                 if change_cnt == 1:
#                     queue.append([words[i], cnt + 1])
#                     visited[i] = 1
#     return answer 
