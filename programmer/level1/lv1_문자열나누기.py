# 정답
def solution(str):
    answer = 0
    x_cnt = 0
    dif_cnt = 0
    for s in str:
        if x_cnt == dif_cnt:
            answer += 1
            x = s
        if x == s:
            x_cnt += 1
        else:
            dif_cnt += 1
            
# def solution(s):
#     s = s.lower()
#     answer = 0
#     if 1<=len(s)<=10000:
#         x_cnt, dif_cnt, cutnum = 0,0,0
#         for i in range(len(s)):
#             x = s[cutnum]
#             if x == s[i]:
#                 x_cnt +=1
#             else:
#                 dif_cnt +=1 
#             if cutnum + 1 == len(s):
#                 answer +=1
#             else:
#                 if x_cnt == dif_cnt:
#                     answer +=1
#                     cutnum = i+1
#     else:
#         return False

#     return answer


        



# def solution(s):
#     answer = 0
#     x_cnt = 0
#     dif_cnt = 0
#     cnt = 0
#     for i in s:
#         if x_cnt == dif_cnt:
#             x = i
#             cnt += 1
#         if x == i:
#             x_cnt += 1
#         else:
#             dif_cnt += 1
#     answer = cnt
#     return answer

