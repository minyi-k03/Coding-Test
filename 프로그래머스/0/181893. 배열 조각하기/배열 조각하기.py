def solution(arr, query):
    
    
    for i in range(len(query)):
        if(i%2==0):
            del arr[query[i]+1:]
        elif i%2!=0:
            del arr[:query[i]]
            
    
    
    return arr