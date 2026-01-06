def solution(array, commands):
    tmp=[]
    
    for i in commands:
        lst=array[i[0]-1:i[1]]
        lst.sort()
        tmp.append(lst[i[2]-1])
    
    
    
    return tmp