# Section 5, Lecture 19
print("hello")
name = "Anna"
print(name)
print(type(name))

message = 'John said to me: "I will see you later" '
print(message)

hello = "Hello world"

print(hello)

# Section 5, Lectures 21 + 22 (Project 2)
# Ask user for name
# for this to work, you have to run the program - won't work just executing in console
name = input("What is your name?")
print(name)

# Ask user for age
age = input("What is your age?") # note input function always turns into string!
age = int(age)
print(age)

# Ask user for city
city = input("What is your city?")
print(city)

# Ask user what he/she enjoys
enjoy = input("What do you enjoy?")
print(enjoy)

print(type(age))


# Create output text
string = "Your name is {}, and you are {} years old. You live in {}, and you love {}."
output = string.format(name, age, city, enjoy)

# Print output to screen
print(output)


A = "part I"
B = "part II"

print(A + " " + B)

C = str(1)

"{1} - {0}".format(A,B)

# Section 5, Lecture 23
"hello".count("e")
text = "Happy Birthday"
print(text.count("a"))
print(text.count("day"))

print(text.lower()) # not  modifying initial string
print(text.upper())
print(text.capitalize())
print(text.title())

text.isupper()
text.istitle()
text.isalpha() # spaces are not letters
"78274238".isdigit()
"happyas283948".isalnum()
"!!!!happyas283948".isalnum()

# Section 5, Lecture 24
x = "happy birthday"
print(x.index("birthday"))
x.find("birthday")
x.find("anna") # -1 if not found, case sensitive!

y = "000000000000happybirthday00000000000"
print(y.strip("0"))
print(y.lstrip("0"))
print(y.rstrip("0"))

name = input("What is your name?").strip() # remove any spaces
print(name)
