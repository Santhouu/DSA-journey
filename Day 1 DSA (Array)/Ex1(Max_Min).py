# Function to find max and min in an array
def find_max_min(arr):
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    print("Maximum:", max_val)
    print("Minimum:", min_val)

# Test
arr = [3, 7, 1, 9, 2]
find_max_min(arr)
