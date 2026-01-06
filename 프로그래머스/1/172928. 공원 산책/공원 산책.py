def solution(park, routes):
    answer = []
    
    row=0 #가로
    col=0 #세로
    
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j]=="S":
                col=i #세로 #y좌표
                row=j #가로 #x좌표
                
                
                
    
    for i in routes:
        current_row=row #시작점 x좌표
        current_col=col #시작점 Y좌표
        
        for step in range(int(i[2])):
            if i[0]=="E" and current_row!=len(park[0])-1 and park[current_col][current_row+1]!="X":
                current_row+=1
                if step == int(i[2])-1:
                    row=current_row
                    
            elif i[0]=="W" and current_row!=0 and park[current_col][current_row-1]!="X":
                current_row-=1
                if step == int(i[2])-1:
                    row=current_row
                    
            elif i[0]=="S" and current_col!=len(park)-1 and park[current_col+1][current_row]!="X":
                current_col+=1
                if step==int(i[2])-1:
                    col=current_col
                    
            elif i[0]=="N" and current_col!=0 and park[current_col-1][current_row]!="X":
                current_col-=1
                if step==int(i[2])-1:
                    col=current_col

                    
                
    
        
    
    return [col,row]