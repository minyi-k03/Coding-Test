def solution(arr, n):
    answer = []
    
    for i in range(0,len(arr),2):
        if len(arr)%2!=0:
            arr[i]=arr[i]+n
    for i in range(1,len(arr),2):
        if len(arr)%2==0:
            arr[i]=arr[i]+n
    
    return arr