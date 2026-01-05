def solution(my_string, alp):
    
    answer=my_string.replace(alp,alp.upper())
    
    if alp not in my_string:
        return my_string
    
    return answer