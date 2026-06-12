numbers = [10, 25, 40, 15, 35]

largest = max(numbers)
second_largest = numbers[0]

for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

print("Second largest element:", second_largest)
