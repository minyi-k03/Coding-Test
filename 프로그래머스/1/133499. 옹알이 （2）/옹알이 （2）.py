#인터넷 참고
def solution(babbling):
    answer = 0
    word=["aya","ye","woo","ma"]
    
    for i in babbling:
        comp=""
        temp=""
        for j in i:
            comp+=j
            if comp==temp:
                break
                
            if comp in word:
                temp=comp
                comp=""
                
        if comp=="":
            answer+=1
            
    return answer