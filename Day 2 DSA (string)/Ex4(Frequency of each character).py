def char_frequency(s):
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    for key, value in freq.items():
        print(f"'{key}' → {value}")

# Test
char_frequency("hello santhu")
