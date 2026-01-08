import sys
input = sys.stdin.readline

user = input()
doctor = input()

print("go" if len(user) >= len(doctor) else "no")