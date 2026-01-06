def solution(arr, queries):
    
    for i in range(len(queries)):
        for j in range(1):
            
            arr[queries[i][j]],arr[queries[i][j+1]]=arr[queries[i][j+1]], arr[queries[i][j]]
            
            
                
    
        
    
    return arr