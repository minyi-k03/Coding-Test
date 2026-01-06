def solution(phone_number):
    answer = ''
    
    print(phone_number[-4:])
    
    while len(answer)!=len(phone_number)-4:
        answer+="*"
        
    answer+=phone_number[-4:]
    
    return answer