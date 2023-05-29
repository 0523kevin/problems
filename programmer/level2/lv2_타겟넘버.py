#원소마다 +, - 기호를 붙여가며 두가지 중에 선택해서 결과를 추출 하는 DFS 방식을 선택합니다
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                return answer
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    
    dfs(0,0)
    return answer