#문제를 잘 읽자 코드는 맞더라도 문제에 부합하지 않는 코드여서 틀린 듯
def solution(s):
    answer = ''
    s=s.split(" ")
    
    for i in s:
        for j in range(len(i)):
            if j%2==0:
                answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        answer+=' '
    
    return answer[:-1]