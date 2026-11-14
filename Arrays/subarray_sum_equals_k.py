def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0

    prefix_count = {0: 1}

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]

        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


nums = [1, 1, 1]
k = 2

print("Number of subarrays:", subarray_sum(nums, k))
