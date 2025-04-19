# Function to find second largest number
def second_largest(arr):
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    if second == float('-inf'):
        return "No second largest element"
    return second

# Test
arr = [12, 35, 1, 10, 34, 1]
print("Second Largest:", second_largest(arr))
