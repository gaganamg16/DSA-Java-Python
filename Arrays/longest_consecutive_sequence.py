def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start counting only from the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest


nums = [100, 4, 200, 1, 3, 2]

print("Longest consecutive sequence length:", longest_consecutive(nums))
