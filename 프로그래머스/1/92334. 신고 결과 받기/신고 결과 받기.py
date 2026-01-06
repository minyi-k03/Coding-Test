from collections  import defaultdict
def solution(id_list, report, k):
    answer = []
    
    report=list(set(report))
    
    user= defaultdict(set)
    
    count=defaultdict(int)
    
    for i in report:
        a,b=i.split() #각각 a=i[0] b=i[2]인상태 i[0]=신고자 i[2] = 신고 당한 유저
        
        user[a].add(b) #각각 신고자와 신고당한 사람을 set 형태로 만들어서 저장
        
        count[b]+=1 # 신고 당한 유저와 그 횟수를 set 형태로 저장
        
    for i in id_list: 
        result=0 #result 변수 초기화
        
        for j in user[i]: #딕셔너리 user[i] 의 value값을 하나하나 꺼냄
            if count[j]>=k: #신고 당한 유저 j를 count에 넣어서 횟수가 k이상인지에 대한 검사
                result+=1 #만약 넘었다면 result값에 1추가
        answer.append(result) #해당 값을 리스트에 추가
    
        
    
    
    
    
    return answer