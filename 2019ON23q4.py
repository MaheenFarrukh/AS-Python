def Check(InString):
    # NumDots = int
    # NumAts = int
    # NumOthers = int
    # x = int
    # Index = int

    NumDots = 0
    NumAts = 0
    NumOthers = 0

    for NextChar in InString:
        if NextChar == '.':
            NumDots = NumDots + 1
        elif NextChar == '@':
            NumAts = NumAts + 1
        elif (NextChar != '.') and (NextChar != '@'):
            NumOthers = NumOthers + 1
        # endif
    # next

    if (NumDots >= 1) and (NumAts == 1) and (NumOthers > 5):
        return True
    else:
        return False
# endfunction


print(Check("Jim98.@skail.com"))
