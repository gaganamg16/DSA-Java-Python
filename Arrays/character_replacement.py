def character_replacement(s, k):
    count = {}
    left = 0
    max_frequency = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        max_frequency = max(max_frequency, count[s[right]])

        window_size = right - left + 1

        if window_size - max_frequency > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


s = "AABABBA"
k = 1

print("Longest Repeating Character Length:",
      character_replacement(s, k))
