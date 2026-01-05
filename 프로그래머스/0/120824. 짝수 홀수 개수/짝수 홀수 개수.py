def solution(num_list):
    answer = [0,0]
    
    for i in num_list:
        if i%2==0:
            answer[0]+=num_list.count(i)
        elif i%2!=0:
            answer[1]+=num_list.count(i)
    
    return answer