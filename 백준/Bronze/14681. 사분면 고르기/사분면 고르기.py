import sys
input = sys.stdin.readline

x = int(input())
y = int(input())

#Quadrant 1
if x > 0 and y > 0: # + +
    print("1")
#Quadrant 2
elif x < 0 and y > 0: # - +
    print("2")
#Quadrant 3
elif x < 0 and y < 0 :# - -
    print("3")
#Quadrant 4
elif x > 0 and y < 0: # + -
    print("4")
