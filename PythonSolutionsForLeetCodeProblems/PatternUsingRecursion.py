# ****
# ***
# **
# *

def patternUsingRecursion(row,col=0,symbol="*"):
    if row>0:
        if row ==col:
            print("")
            patternUsingRecursion(row=row-1,col=0)
        else:
            print(symbol,end="")
            patternUsingRecursion(row,col=col+1)
patternUsingRecursion(4)