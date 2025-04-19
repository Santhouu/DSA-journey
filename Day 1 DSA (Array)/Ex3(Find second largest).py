# Function to find second largest number
def second_largest(arr):
    largest = second = float('-inf')

    # iterating all ellements in arr
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    # final check up 
    if second == float('-inf'):
        return "No second largest element"
    return second

# Test
arr = [12, 35, 1, 10, 34, 1]
print("Second Largest:", second_largest(arr))
