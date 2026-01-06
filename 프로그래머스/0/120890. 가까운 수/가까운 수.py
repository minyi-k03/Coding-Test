def solution(array, n):
    answer = 0
    array.sort()
    lst=[]
    for i in array:
        lst.append(abs(n-i))
        
    answer+=array[lst.index(min(lst))]
    print(array)
    
    return answer