def solution(progresses, speeds):
    answer = []
    complete = 0
    days = 0
    
    
    
    while True:
        tmp_progresses = progresses[0]
        tmp_speeds = speeds[0]
        
        if tmp_progresses + tmp_speeds*days >= 100: #기능 개발을 완료한 경우
            complete += 1
            tmp_progresses = progresses.pop(0)
            tmp_speeds = speeds.pop(0)
            
        else:
            if complete > 0:
                answer.append(complete)
                complete = 0
                
            else:
                days += 1
                
        if len(progresses) == 0:
            answer.append(complete)
            break
    
    
    
                
        
                
                
    
    
    return answer