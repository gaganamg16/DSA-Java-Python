def first_unique_character(s):
    for char in s:
        if s.count(char) == 1:
            return char

    return None


text = "leetcode"

result = first_unique_character(text)

if result:
    print("First unique character:", result)
else:
    print("No unique character found")
    
