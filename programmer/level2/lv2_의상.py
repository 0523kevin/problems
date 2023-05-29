from collections import Counter
def solution(clothes):
    answer = 1
    dic_clothes = dict(clothes)
    kind = dic_clothes.values()
    cnt_kind = Counter(kind)
    value_kind = cnt_kind.values()
    for i in value_kind:
        answer *= (i+1)
            
    return answer - 1