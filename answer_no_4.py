# take input string
input_string = "hello world"

# create dictionary to store character counts
char_counts = {}

# iterate through string and count occurrences of each character
for char in input_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# sort dictionary by UTF-8 code point
sorted_char_counts = sorted(char_counts.items(), key=lambda x: ord(x[0]))

# print results
for char, count in sorted_char_counts:
    print(f"{char}: {count}")
