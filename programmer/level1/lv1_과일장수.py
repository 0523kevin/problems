# 정답
def solution(k,m,score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        box = score[i:i+m]
        if len(box) == m:
            answer += m * box[-1]
    return answer

# 간출임
def solution(k,m,score):
    answer = 0
    score.sort(reverse = True)
    for i in range(m-1,len(score),m):
        answer += score[i]*m
    return answer
       