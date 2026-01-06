def solution(arr):
    answer = []
    arr_index=[i for i,value in enumerate(arr) if value==2]
    
    if arr_index==[]:
        return [-1]
    elif len(arr_index)==1:
        return [2]
    else:
        
        return arr[arr_index[0]:arr_index[-1]+1]
    
    