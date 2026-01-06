def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i]==True:
            for j in range(arr[i]):
                answer.append(arr[i])
                answer.append(arr[i])
        elif flag[i]==False:
            for j in range(arr[i]):
                del answer[-1]
    
    print(answer)
    return answer