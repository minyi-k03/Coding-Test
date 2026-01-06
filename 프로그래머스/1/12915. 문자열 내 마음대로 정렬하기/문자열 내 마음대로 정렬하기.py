def solution(strings, n):
    answer=[]
    tmp_locate=[]
    
    for i in strings:
        answer.append(i[n]+i)
    answer.sort()
    print(answer)
    return [i[1:] for i in answer]