def solution(k, score):
    answer = []
    top = []
    for i in score:
        top.append(i)
        top.sort(reverse = True)
        if len(top)<=k:
            answer.append(top[-1])
        else:
            top.pop(-1)
            print(top)
            answer.append(top[-1])            
    return answer