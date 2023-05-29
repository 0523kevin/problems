# 정답
def solution(elements):
    answer = 0 
    sum_lst = set()
    new_lst = elements*2
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            sum_lst.add(sum(new_lst[j:j+i]))
    answer = len(sum_lst)
    return answer



# 나의 로직 다시 푼것
def solution(elements):
    answer = 0 
    sum_lst = set()
    new_lst = elements*2
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            sum_lst.add(sum(new_lst[j:j+i]))
    answer = len(sum_lst)
    return answer



# 시간 초과, 틀림
# def solution(elements):
#     answer = 0
#     sum_lst = list()
#     for i in range(1,len(elements)+1):
#         elements = add_lst(elements,i)
#         if i == len(elements):
#             sum_lst.append(sum(elements))
#         for j in range(len(elements)-i):
#             res = sum(elements[j:(j+i)])
#             sum_lst.append(res)
#     answer = len(set(sum_lst))
#     return answer

# def add_lst(lst, num):
#     for i in range(num-1):
#         lst.append(lst[i])
#     return lst

