# Function to reverse a string
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepending each character
    return reversed_str

# Test
text = "Santhu"
print("Reversed:", reverse_string(text))
