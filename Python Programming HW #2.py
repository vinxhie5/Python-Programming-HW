yr = int(input("Enter a year: "))

if yr % 4 == 0 and yr % 100 != 0:
    print("The year ",yr, "is a Leap Year")
elif yr % 100 == 0:
    print("The year ",yr, "is not a Leap Year")
elif yr % 400 ==0:
    print("The year ",yr, "is a Leap Year")
else:
    print("The year ",yr, "is not a Leap Year")