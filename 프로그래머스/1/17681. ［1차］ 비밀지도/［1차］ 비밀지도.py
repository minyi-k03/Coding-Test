def solution(n, arr1, arr2):
    answer = []
    clue_lst1=[]
    clue_lst2=[]
    clue_str=""
    for i in arr1: #2진수 변환
        i=format(i,'b')
        i=str(i)
        clue_lst1.append(i.zfill(n))
        
    for i in arr2: #2진수 변환
        i=format(i,'b')
        i=str(i)
        clue_lst2.append(i.zfill(n))
        
    
    for i in range(n):
        for j in range(n):
            if int(clue_lst1[i][j])==1 and int(clue_lst2[i][j])==0:
                clue_str+="#"
            elif int(clue_lst1[i][j])==0 and int(clue_lst2[i][j])==1:
                clue_str+="#"
            elif int(clue_lst1[i][j])==1 and int(clue_lst2[i][j])==1:
                clue_str+="#"
            elif int(clue_lst1[i][j])==0 and int(clue_lst2[i][j])==0:
                clue_str+=" "
              
    for i in range(0,len(clue_str),n):
        answer.append(clue_str[i:i+n])
    
    return answer