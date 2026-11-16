from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    target_count = Counter(t)
    window_count = {}

    have = 0
    need = len(target_count)

    left = 0
    min_length = float("inf")
    result = ""

    for right in range(len(s)):
        char = s[right]

        window_count[char] = window_count.get(char, 0) + 1

        if char in target_count and window_count[char] == target_count[char]:
            have += 1

        while have == need:
            window_length = right - left + 1

            if window_length < min_length:
                min_length = window_length
                result = s[left:right + 1]

            left_char = s[left]
            window_count[left_char] -= 1

            if (left_char in target_count and
                window_count[left_char] < target_count[left_char]):
                have -= 1

            left += 1

    return result


s = "ADOBECODEBANC"
t = "ABC"

print("Minimum window substring:", min_window(s, t))
