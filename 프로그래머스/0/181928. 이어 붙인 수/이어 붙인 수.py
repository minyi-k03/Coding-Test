def solution(num_list):
    lst=[]
    lst2=[]
    
    for i in range(len(num_list)):
        if(num_list[i]%2==0):
            lst.append(str(num_list[i]))
        elif(num_list[i]%2!=0):
            lst2.append(str(num_list[i]))
    total=''.join(lst)
    total2=''.join(lst2)
    total=int(total)
    total2=int(total2)
    answer=total+total2
    return answer