def index_power(array, n):
    if n < 0 or n >= len(array):
        return -1
    return array[n] ** n


print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 2, 3], 3)) 