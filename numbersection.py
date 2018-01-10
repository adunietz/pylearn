# Section 4, Lecture 2
2 + 3

100-20

2 * 2

2/4

print(type(2))
print(type(0.5))

# modulo
5 % 3

7.5 % 5

# Section 4, Lecture 3
2*(5-1)

# Section 4, Lectures 4 and 5
import random # should be at top of file, but whatever :)
health = 50
difficulty = 3
print("initial health:", health)
potion_health = int(random.randint(25, 50)/difficulty) # convert into integer via "casting"

health = health + potion_health
print("final health:", health)
print("potion health:", potion_health)

# Section 4, Lectures 6
import math
print(round(2.1))
print(round(1.5))
print(math.floor(1.5))
print(math.ceil(2.1))
print(math.pi)
print(math.e)
print(math.floor(math.sin(math.pi)))
print(math.cos(0))
print(math.asin(0))
print(math.acos(0))
print(math.hypot(3,4))
print(math.pow(2,3))
print(2**3)
print(math.exp(2))
print(math.log(math.e))
print(math.log10(1000))

