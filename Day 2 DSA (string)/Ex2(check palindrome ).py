# A palindrome reads the same forward and backward
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Handle case and spaces
    return s == s[::-1]

# Test
print(is_palindrome("madam"))      # True
print(is_palindrome("Santhu"))     # False
