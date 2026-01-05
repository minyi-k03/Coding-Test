def solution(arr1, arr2):
    answer = 0
    
    if(len(arr1)<len(arr2)):
        return -1
    elif(len(arr1)>len(arr2)):
        return 1
    elif(len(arr1)==len(arr2)):
        total=sum(arr1)
        total2=sum(arr2)
        
        if(total>total2):
            return 1
        elif total<total2:
            return -1
        elif total==total2:
            return 0
        
            
    
    