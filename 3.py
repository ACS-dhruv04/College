def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]
numbers = [10,20,30,40,50]
print("Second largest:", second_largest(numbers))
