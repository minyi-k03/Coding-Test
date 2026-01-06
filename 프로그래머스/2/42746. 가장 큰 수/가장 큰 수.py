def solution(numbers):
    string_num = []
    for i in numbers:
        string_num.append(str(i))
        
        
    from functools import cmp_to_key
    
    def compare_strings(a,b):
        option1 = int(a+b)
        option2 = int(b+a)
        
        return option1 - option2
    
    string_num.sort(key = cmp_to_key(compare_strings), reverse = True)
    
    final_answer = "".join(string_num)
    
    if int(final_answer) == 0:
        return "0"
    
    
    return final_answer