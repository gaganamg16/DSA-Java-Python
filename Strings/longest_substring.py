def longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right

        max_length = max(max_length, right - left + 1)

    return max_length


text = "abcabcbb"

result = longest_substring(text)

print("Longest substring length:", result)