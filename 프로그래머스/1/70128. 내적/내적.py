def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        total=a[i]*b[i]
        answer+=total
    return answer