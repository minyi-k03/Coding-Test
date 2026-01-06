def solution(str1, str2):
    lst1=list(str1)
    lst2=list(str2)
    lst3=[]
    
    for i in range(0,len(str1)):
        lst3.append(lst1[i])
        lst3.append(lst2[i])
        
    
    answer = ''.join(lst3)
    return answer