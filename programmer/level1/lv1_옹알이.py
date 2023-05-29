# 정답
def solution(babbling):
    answer = 0
    key = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        word = word.lower()
        for k in key:
            if k in word:
                if k+k not in word:
                    word = word.replace(k,' ')  # 문자열 삭제 하면서 띄어쓰기 해줘야 삭제 후 생기는 단어가 k 중 하나로 생성되는 것을 막는다.
        if word.rstrip() == '':
            answer += 1

    return answer


# v0.1
# def solution(babbling):
#     answer = 0
#     key = ['aya', 'ye', 'woo', 'ma']
#     cnt = 0
#     for word in babbling:
#         word.lower()
#         for k in key:
#             if k in word:
#                 if k*2 in word:
#                     cnt = 0
#                 else:
#                     cnt += 1
#                     for i in range(len(word)-1):
#                         if word[i] != word[i+1]:
#                             continue   
#                         else:
#                             cnt = 0
#                             if 'woo' in word:
#                                 cnt += 1       
                    
#         if cnt>=1:  
#             answer += 1
#         cnt = 0

#     return answer