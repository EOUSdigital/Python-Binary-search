def binary_search(data, target):

    left = 0
    right = len(data) - 1
    found = False

    while left <= right and not found:
        mid = (left + right) // 2           # Calculate middle index

        if data[mid] == target:
            found = True
        elif data[mid] < target:
            left = mid + 1                  # Search right half
        else:
            right = mid - 1                 # Search left half
    
    if found:
        return True, mid
    else:
        return False, -1

numbers = [34, 68, 12, 89, 90, 44, 18, 57, 23, 61]
item_to_find = 44

result = binary_search(numbers, item_to_find)
print(f"Found: {result[0]}, Position: {result[1]}")