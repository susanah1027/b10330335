#計算機

numbers = []
while True:
    x = input("enter a number or Enter to finish:")
    if x is not "":
        y = int(x)
        numbers.append(y)
    else:
        break

print("count:", len(numbers))
print("sum:", sum(numbers))
print("lowest:", min(numbers))
print("highest:", max(numbers))
print("mean:",sum(numbers)/ len(numbers))


