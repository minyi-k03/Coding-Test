def solution(new_id):
    answer = ''
    new_id=new_id.lower() #1단계
    
    for i in new_id: #2단계
        if i.isalnum() or i=="-" or i=="_" or i==".":
            answer+=i
            
    while ".." in answer: #3단계
        answer=answer.replace("..",".")
    
    if answer[0]==".": #4단계
        if len(answer)>1:
            answer=answer[1:]
        else:
            "."
    if answer[-1]==".":
        answer=answer[:-1]
        
    if answer=="": #5단계
        answer="a"
    
    if len(answer)>15: #6단계
        answer=answer[:15]
        if answer[-1]==".":
            answer=answer[:14]
        
        
            
    if len(answer)<=2:
        while len(answer)!=3:
            answer+=answer[-1]
        
    return answer