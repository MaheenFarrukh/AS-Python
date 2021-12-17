# StudentName = str
# C = int
# Temp, Ielement, relement = str
# NameLength, i, lchar, rchar = int
# UnusedCount = int
# stemp = str
# swapped = bool

StudentName = ["salman", "kamran", "bashir", "zohaib", "mohsin", "ali", "####", "####", "####", "####"]
dumval = "####"
i = 10
UnusedCount = 0

for C in range(10):
    if StudentName[C] == dumval:
        UnusedCount = UnusedCount + 1
    else:
        NameLength = len(StudentName[C])
        Temp = StudentName[C][:1]
        Temp = Temp.upper()
        StudentName[C] = Temp + StudentName[C][NameLength - 1:]
    # endif
# next

swapped = True
while swapped is True:
    swapped = False
    for C in range(i-1):
        lelement = StudentName[C][:1]
        relement = StudentName[C + 1][:1]
        lchar = ord(lelement)
        rchar = ord(relement)
        if lchar > rchar:
            stemp = StudentName[C]
            StudentName[C] = StudentName[C + 1]
            StudentName[C + 1] = stemp
            swapped = True
        # endif
    # next
# endwhile


for C in range(10):
    print("The studentname ", StudentName[C])
# next

print("There are = ", UnusedCount)
