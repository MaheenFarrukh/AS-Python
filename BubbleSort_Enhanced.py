swapped = bool
temp = int
maxsize = 5
height = [0]*6

for count in range(0, 5):
    height[count] = int(input("Enter Height of a student in centimeters:"))
# next
# sort the elements

while swapped is not False:
    swapped = False
    for count in range(0, maxsize-1):
        if height[count+1] < height[count]:
            temp = height[count]
            height[count] = height[count+1]
            height[count+1] = temp
            swapped = True
        # endif
    # next
    maxsize = maxsize-1
# endwhile

for count in range(0, 5):
    print(count, ":", height[count])
# next
