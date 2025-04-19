# Function to reverse an array
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        # Swap
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

# Test
arr = [1, 2, 3, 4, 5]
print("Reversed Array:", reverse_array(arr))
