#해답
def solution(ingredient):
    if len(ingredient)>1000000 or len(ingredient)<1:
        exit
    answer = 0
    stack = list()
    for burger in ingredient:
        stack.append(burger)
        if stack[-4:] == [1,2,3,1]:
            answer += 1            
            for i in range(4):
                stack.pop()
    return answer


# 내 해답 - 오래걸림, 시간초과
def solution(ingredient):
    if len(ingredient)>1000000 or len(ingredient)<1:
        exit
    hamberger = [1,2,3,1]
    answer = 0
    i = 0
    while True:
        if hamberger == ingredient[i:i+4]:
            del ingredient[i:i+4]
            answer += 1
            i=0
        else:
            i += 1
        if i == len(ingredient):
            break
            
    return answer




        