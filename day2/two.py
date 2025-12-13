a=int(input("ENTER A NUMBER:"))
if(a%2==0):
    print("EVEN NUMBER")
    if(a%4==0):
        print("DIVISIBLE BY 4")
    else:
        print("NOT DIVISIBLE BY 4")
else:
    print("ODD NUMBER")