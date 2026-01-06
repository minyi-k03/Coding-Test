def convert(number,n):
    NUMBER = '0123456789ABCDEF'
    tmp = ''
    
    if number == 0:
        return '0'
    
    while number > 0:
        number,remain = divmod(number,n) #number을 n진수로 나눈 몫과 나머지를 출력
        tmp += NUMBER[remain]
        
    return tmp[::-1]
        
    

def solution(n, t, m, p):
    answer = ''
    game = ''
    order = p-1
    
    for i in range(t*m):
        game += convert(i,n)
        
        
    while True:
        if len(answer) == t:
            break
            
        answer += game[order]
        
        order += m

    
    
    return answer