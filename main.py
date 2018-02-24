  # http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
uNum = int(input("Enter a number: "))  # why did i look up for statements
if (uNum%2) == 0:
    if(uNum%4 == 0):
        print(str(uNum)+" is a multiple of 4!! ")
    else:
       print(str(uNum)+" is an even number!")
else:
    print(str
          (uNum)+" is an Odd number!")