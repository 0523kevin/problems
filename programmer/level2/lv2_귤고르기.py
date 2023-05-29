from collections import Counter
def solution(k, tangerine):
    answer = 0
    dic_tan = Counter(tangerine)
    tot = 0
    for i, v in enumerate(sorted(dic_tan.values(),reverse = True)):
        tot += v
        if tot>=k:
            answer = i+1
            break
    return answer