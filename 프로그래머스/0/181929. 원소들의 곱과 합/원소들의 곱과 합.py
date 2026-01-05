def solution(num_list):
    total=1
    total2=0
    answer=0
    for i in range(len(num_list)):
        total*=num_list[i] #모든 원소들의 곱
        total2+=num_list[i] #모든 원소들의 합의 제곱
        
        if(total<pow(total2,2)):
            answer=1
        elif(total>pow(total2,2)):
            answer=0
    
    return answer