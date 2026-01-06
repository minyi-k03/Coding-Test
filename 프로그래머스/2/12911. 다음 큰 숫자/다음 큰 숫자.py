def solution(n):
    
    trade_num=format(n,'b')
    default_num=n
    while True:
        default_num+=1
        compare_num=format(default_num,'b')
        if default_num>n and compare_num.count('1')==trade_num.count('1'):
            return default_num
            break
            
            
    