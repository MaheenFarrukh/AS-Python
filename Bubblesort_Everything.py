height = [45, 67, 23, 45, 21, 78, 90, 11, 21]

swapped = bool  # declare as boolean variable
temp = int  # declare as integer
counter = int(0)  # declare as integer
# counter = 0
count = int
while swapped is not False:
    swapped = False
    # for x = 0 to 8
    for count in range(0, 8):
        if height[count+1] < height[count]:
            temp = height[count]
            height[count] = height[count+1]
            height[count+1] = temp
            swapped = True
        # endif
        counter = counter + 1
    # next
# endwhile # loop until swapped = False
# Print out the elements

for count in range(0, 8):
    print(count, ":", height[count])
# next
print("the algo analysis : ", counter)

# import msvcrt
# print("Press any key to quit")
