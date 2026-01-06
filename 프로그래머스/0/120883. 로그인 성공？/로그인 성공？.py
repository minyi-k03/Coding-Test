def solution(id_pw, db): #아이디 패스워드, 회원정보
    
    answer = ''
    for i in range(len(db)):
        if id_pw[0]==db[i][0] and id_pw[1]==db[i][1]:
            return "login"
        elif id_pw[0]==db[i][0] and id_pw[1]!=db[i][1]:
            return "wrong pw"
            
            
            
    return "fail"