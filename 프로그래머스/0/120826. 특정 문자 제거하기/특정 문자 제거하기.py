def solution(my_string, letter):
    answer = ''
    
    for _ in range(len(my_string)):
        if letter in my_string:
            my_string=my_string.replace(letter,"")
    
    
    return my_string