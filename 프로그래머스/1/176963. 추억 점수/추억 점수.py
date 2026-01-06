def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    yearn_dict={}
    tmp=0
    count=0
    for i in range(len(name)):
        yearn_dict[name[i]]=yearning[i]
    
    for i in photo:
        for j in i:
            if j in yearn_dict.keys():
                answer[count]+=yearn_dict[j]
        count+=1
            
    
    return answer