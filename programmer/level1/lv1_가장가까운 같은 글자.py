def solution(s):
	answer = []
	marked = {}
	for k, v in enumerate(list(s)):
		if v not in marked.keys():
			marked[v] = k
			answer.append(-1)
		else:
			l = k - marked[v]
			answer.append(l)
			marked[v] = k
	return answer