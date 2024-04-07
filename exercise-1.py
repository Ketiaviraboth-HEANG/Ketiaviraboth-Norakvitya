def replace_last(numbers):
    if len(numbers) <= 1:
        return numbers
    last_element = numbers.pop()  
    numbers.insert(0, last_element)  
    return numbers


print(replace_last([2, 3, 4, 1]))