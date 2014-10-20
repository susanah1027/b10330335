#if else 
x = int(input("What animal do you prefer:"))

if x < 0:
    x = 0
    print("zebra")
elif x == 0:
    print("lion")
elif x == 1:
    print("panda")
else:
    print("kangaroo")


