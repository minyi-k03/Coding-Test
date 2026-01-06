def solution(my_string, s, e):
    answer = ''
    value = my_string[s:e+1][::-1]
    
    return my_string[:s]+value+my_string[e+1:]