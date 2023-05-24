def add_multiples_three_five(number):
    sum = 0
    for i in range(1, number + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(add_multiples_three_five(10))
print(add_multiples_three_five(20))
print(add_multiples_three_five(15))
