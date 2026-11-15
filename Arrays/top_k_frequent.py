from collections import Counter
import heapq


def top_k_frequent(nums, k):
    frequency = Counter(nums)

    result = heapq.nlargest(
        k,
        frequency.keys(),
        key=frequency.get
    )

    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2

print("Top K frequent elements:", top_k_frequent(nums, k))
