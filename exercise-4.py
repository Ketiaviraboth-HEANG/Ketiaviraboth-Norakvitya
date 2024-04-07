from math import ceil

def chunking_by(lst, size):
    if not lst:
        return []
    return [lst[i:i+size] for i in range(0, len(lst), size)]


print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))  