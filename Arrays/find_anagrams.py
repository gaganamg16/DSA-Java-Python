def find_anagrams(s, p):
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    window_count = [0] * 26

    for ch in p:
        p_count[ord(ch) - ord('a')] += 1

    result = []
    window_size = len(p)

    for i, ch in enumerate(s):
        window_count[ord(ch) - ord('a')] += 1

        if i >= window_size:
            old_char = s[i - window_size]
            window_count[ord(old_char) - ord('a')] -= 1

        if window_count == p_count:
            result.append(i - window_size + 1)

    return result


s = "cbaebabacd"
p = "abc"

print("Anagram starting indices:", find_anagrams(s, p))
