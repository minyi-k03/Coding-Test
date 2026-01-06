def solution(my_string):
    answer = ''
    
    for i in my_string:
        if 65<=ord(i)<=90:
            answer+=i.lower()
        elif 97<=ord(i)<=122:
            answer+=i.upper()
            
    
    return answer