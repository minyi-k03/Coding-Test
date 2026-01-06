#filter함수를 알아야 함
def solution(myString):
    answer = []
    
    myString=list(filter(None,myString.split("x")))
    
    return sorted(myString)