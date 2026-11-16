from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("Grouped anagrams:", group_anagrams(words))
