def solution(numbers, direction):
    answer = []
    
    
    if direction=="right":
        for j in range(-1,len(numbers)-1):
            answer.append(numbers[j])
    elif direction=="left":
        for j in range(1,len(numbers)):
            answer.append(numbers[j])
            
        answer.append(numbers[0])
    
    
    return answer