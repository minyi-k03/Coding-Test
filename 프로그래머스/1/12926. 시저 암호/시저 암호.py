def solution(s, n):
    answer = ''
    
    big_alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
              "V","W","X","Y","Z"]
    
    small_alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
                "v","w","x","y","z"]
    
    
    
    for i in s:
        if i in big_alpha: #대문자 경우
            location=big_alpha.index(i)+n
            if location>=len(big_alpha):
                location=abs(len(big_alpha)-location)
                answer+=big_alpha[location]
            else:
                answer+=big_alpha[location]
            
        elif i in small_alpha: #소문자 경우
            location=small_alpha.index(i)+n
            if location>=len(small_alpha):
                location=abs(len(small_alpha)-location)
                answer+=small_alpha[location]
            else:
                answer+=small_alpha[location]
                
        else:
            answer+=i
            
            
        
    
    
    
    return answer