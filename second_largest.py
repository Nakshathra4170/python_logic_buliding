numbers = [10, 25, 40, 15, 35]

largest = numbers[0]
secondlargest = numbers[0]

for i in numbers[1:]:
    if i > largest:
        secondlargest = largest
        largest = i
    elif i > secondlargest and i != largest:
        secondlargest = i

print("Second largest:", secondlargest)
