# Section 6, Lecture 30

B = True # need to capitalize Booleans
C = False
print(type(B))

2 > 3

2 == 3
3==3

3 != 3
2 != 3
4 >= 3
4 <= 3

# Section 6, Lecture 31
if 3<2:
    print("It worked")

num1 = 10
num2 = 10

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("Both nums equal")

# Section 6, Lecture 32
# not operator
not 1>3

C = 1
D = 5

#if C > 10 and D > 1:
#    print("It worked")

if not (C > 10 and D > 1):
    print("It worked")

# Section 6, Lecture 33
C = 6
D = 2

if C>1 or D>1:
    print("Working")