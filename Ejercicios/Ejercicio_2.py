def sum_even_numbers(numbers):
    total_sum = 0
    for number in numbers:
        if number % 2 == 0:
            total_sum += number
    return total_sum

print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
print(sum_even_numbers([10, 20, 30, 40]))
print(sum_even_numbers([15, 25, 35, 45]))
