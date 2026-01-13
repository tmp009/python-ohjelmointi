def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_even_numbers(numbers)

print(f"Original list: {numbers}")
print(f"List with even numbers only: {filtered_numbers}")
