def reverse_ascending(items):
    result = []
    subsequence = []
    for item in items:
        if not subsequence or item > subsequence[-1]:
            subsequence.append(item)
        else:
            result.extend(subsequence[::-1])
            subsequence = [item]
    result.extend(subsequence[::-1])
    return result


print(list(reverse_ascending([1, 2, 3, 4, 5])))  
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))  
print(list(reverse_ascending([5, 4, 3, 2, 1])))  
print(list(reverse_ascending([])))  