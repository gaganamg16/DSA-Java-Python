def maximum_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = maximum_subarray(nums)

print("Maximum subarray sum:", result)