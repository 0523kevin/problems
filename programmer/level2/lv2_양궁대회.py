def solution(n, info):

    def get_areal_score(areal_point, a_shots, l_shots):
        a_areal_score, l_areal_score = 0,0
        if l_shots > a_shots:
            l_areal_score = areal_point
        elif a_shots > 0:
            a_areal_score = areal_point
        return a_areal_score, l_areal_score

    def get_total_score(a_scores, l_scores):
        a_total, l_total = 0, 0
        for index, (a_shots, l_shots) in enumerate(zip(a_scores, l_scores)):
            a_areal_score, l_areal_score = get_areal_score(10 - index, a_shots, l_shots)
            a_total += a_areal_score
            l_total += l_areal_score
        return a_total, l_total

    def recursive(l_scores, shots):
        nonlocal answers, l_max
        if shots > n:
            return
        if len(l_scores) == 11:
            if shots == n:
                a_score, l_score = get_total_score(info, l_scores)
                if (diff := l_score - a_score) >= l_max:
                    l_max = diff
                    answers.setdefault(diff, [])
                    answers[diff].append(l_scores)
            return
        for each in range(n+1):
            recursive(l_scores + [each], shots + each)

    l_max = 0
    answers = {}
    recursive([], 0)
    return sorted(answers[l_max], key = lambda x: (x[10], x[9], x[8], x[7], x[6], x[5], x[4], x[3], x[2], x[1], x[0]))[-1] if l_max > 0 else[-1]




def solution(n, a_scores):
    def getscore(r_scores):
        tot = 0
        for i in range(len(a_scores)):
            if a_scores[i] < r_scores[i]:
                tot += 10-i
            elif a_scores[i] > 0:
                tot -= 10-i
        return tot
    
    def recursive(idx, left, r_scores):
        nonlocal answer, max_score
        if idx == -1 and left:
            return
        if left == 0:
            score = getscore(r_scores)
            if max_score < score:
                answer = r_scores.copy()
                max_score = score
            return
        for i in range(left, -1, -1):
            r_scores[idx] = i
            recursive(idx-1, left-i, r_scores)
            r_scores[idx] = 0
    
    max_score = 0
    answer = [0 for _ in range(n+1)]
    recursive(10, n, [0 for _ in range(11)])
    return [-1] if max_score == 0 else answer

