def remove_dupi(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
        return result

num = [1, 2, 2, 3, 4, 4, 5]
print("Without Duplicates : ", remove_dupi(num))