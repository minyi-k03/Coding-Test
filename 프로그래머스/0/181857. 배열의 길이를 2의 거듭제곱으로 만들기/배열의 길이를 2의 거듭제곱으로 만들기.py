def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if (len(arr)&(len(arr)-1)):
            arr.append(0)
        else:
            return arr
        
    
    
    