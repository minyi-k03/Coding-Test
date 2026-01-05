def solution(myString, pat):
    answer = 0
    
    myString=list(myString)
    
    for i in range(len(myString)):
        if myString[i]=='A':
            myString[i]='B'
        elif myString[i]=='B':
            myString[i]='A'
            
    if pat in "".join(myString):
        answer=1
    else:
        answer=0
    
    
    
    return answer