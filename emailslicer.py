# Section 5, Lectures 25+
string = "ABCDEFG123456"

word = "supercalifragilisticexpialidocious"
print(word[0])
print(word[2])

print(word[0:5:3])
print(word[0:5])
print(word[5:])
print(word[5::2])
print(word[:7])
print(word[::-1])
print(word[::-3]) # reverse and take every 3rd letter
print(word[-2]) # to count from "end" value

print(word[word.index("cali"):word.index("fragi")]) # note index only finds first case of this

word = "asdfadestablishment23748kasdf"
print(word[word.index("establishment")])

