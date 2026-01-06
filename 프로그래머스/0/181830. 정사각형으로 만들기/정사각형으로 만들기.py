def solution(arr):
    answer = [[]]
    col=len(arr) #세로 
    row=len(arr[0]) #가로
    count=col
    if row<col: #가로<세로
        for i in range(col):
            for j in range(col-row):
                arr[i].append(0)
    elif row>col: #세로>가로
        for i in range(row-col):
            arr.append([0]*row)
    else:
        return arr
    
    return arr