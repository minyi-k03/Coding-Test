def solution(letter):
    answer = []
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    letter=letter.split(' ') #이거 빼먹어서 안풀림
    print(letter)
    for i in letter:
        answer.append(morse[i])
        
    
    return "".join(answer)