def solution(s):
    answer = True
    stack = []
    if s.startswith(')') or s.endswith('('):
        answer = False
    else:
        if s.count('(') != s.count(')'):
            answer = False
        else:
            for i in s:
                if stack == []:
                    stack.append(i)
                    continue
                if stack[0] == ')':
                    answer = False
                    break
                elif stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    stack.append(i)
    return answer
        
# #정답
# def solution(s):
#     answer = True
#     stack = []
#     cnt1 = s.count('(')
#     cnt2 = s.count(')')
#     if len(s) % 2 != 0:
#         answer = False
#     else:
#         if s.startswith('(') and s.endswith(')'):
#             if cnt1 != cnt2:
#                 answer = False
#             else:
#                 for i in s:
#                     if i == '(':
#                         stack.append(i)
#                     else:
#                         if stack == []:
#                             answer = False
#                         else:
#                             stack.pop()
                        
#         else:
#             answer = False

#     return answer