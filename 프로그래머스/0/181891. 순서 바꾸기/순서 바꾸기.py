def solution(num_list, n):
    answer = []
    answer.append(num_list[n:])
    answer.append(num_list[0:n])
    answer=sum(answer,[])
    return answer