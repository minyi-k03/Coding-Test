def solution(a, b):
    a,b=str(a),str(b)
    num=2*int(a)*int(b)
    
    if(int(a+b)>=num):
        return int(a+b)
    else:
        return num