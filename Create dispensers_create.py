DISPENSERS = open("C:\\Users\\mahee\\OneDrive\\Desktop\\GitHub Python\\DISPENSERS.txt", "w")
DISPENSERS.DispenserCode = input("Enter dispenser code (XXXXX to end)")
while DISPENSERS.DispenserCode != "XXXXX":
    if DISPENSERS.DispenserCode != "XXXXX":
        DISPENSERS.BankCode = input("Enter bank code...")
        LineString = DISPENSERS.DispenserCode + " " + DISPENSERS.BankCode
        # now write the new line to the file
    # endif
    DISPENSERS.DispenserCode = input("Enter dispenser code (XXXXX to end)")
# endwhile
DISPENSERS.close()
print("DISPENSERS file now created")
