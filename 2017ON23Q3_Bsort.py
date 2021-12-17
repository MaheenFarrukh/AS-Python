UserNameArray = ["567843Kamran", "765345Ali", "234543shameer", "1123432InduaraMethamal", "345654Shahroshano", "665432MrSadiqHussain"]
swapped = bool
temp = str
x1 = str
x2 = str
maxsize = 5

while swapped is not False:
    swapped = False
    for count in range(0, maxsize-1):
        x1 = (UserNameArray[count][:6])
        x2 = (UserNameArray[count + 1][:6])
        if x2 < x1:
            temp = UserNameArray[count]
            UserNameArray[count] = UserNameArray[count + 1]
            UserNameArray[count + 1] = temp
            swapped = True
        # endif
    # next
    maxsize = maxsize - 1
# endwhile

for count in range(0, 5):
    print(count, ":", UserNameArray[count])
# next
