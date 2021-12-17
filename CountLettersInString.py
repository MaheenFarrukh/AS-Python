# str1 = str
# count = int
# NC = str
# letter = str

count = 0
str1 = str(input("Enter String: "))
letter = str(input("Enter letter: "))
for n in str1:
    # NC = str1[n:1]
    if n == letter:
        count = count + 1
    # endif
# next
print("the ans : ", count)
