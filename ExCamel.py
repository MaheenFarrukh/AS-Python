def ExCamel(InString):
    # NextChar = str
    # OutString = str
    # n = int
    OutString = ""  # initialise the return string
    # loop through InString to produce OutString

    for NextChar in InString:  # from first to last
        # NextChar = InString[n:1]  # get next character
        if NextChar == NextChar.upper():  # check if uppercase
            if NextChar != InString[1:1]:  # if not first character
                OutString = OutString + " "  # add space to OutString
            # endif
            NextChar = NextChar.lower()  # make NextChar lower case
        # endif
        OutString = OutString + NextChar  # add NextChar to OutString
    # next
    return OutString  # return value
# end def


print(ExCamel("Waluigi Hehe"))
