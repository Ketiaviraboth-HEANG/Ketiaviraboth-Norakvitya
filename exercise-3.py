def remove_all_after(lst, border):
    try:
        index = lst.index(border)
        return lst[:index + 1]
    except ValueError:
        return lst


print(remove_all_after([1, 2, 3, 4, 5], 3))       
print(remove_all_after([1, 1, 2, 2, 3, 3], 2))    
print(remove_all_after([], 5))                     