def common_elements(list_1, list_2):
    elements = []
    for element in list_1:
        if element in list_2:
            elements.append(element)
    return elements

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print(common_elements([10, 20, 30], [30, 40, 50]))
print(common_elements(['a', 'b', 'c'], ['b', 'c', 'd']))
