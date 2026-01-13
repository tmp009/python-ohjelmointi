def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers_input = [10, 4, 1]
result = sum_of_list(numbers_input)
print(f"The sum of the numbers in the list is: {result}")
