def solution(s):
    answer = []
    s=list(s)
    for i in s:
        if s.count(i)==1:
            answer.append(i)
        
    answer.sort()
    return "".join(answer)