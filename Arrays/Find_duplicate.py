def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Find the intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # Find the entrance to the cycle
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [1, 3, 4, 2, 2]

print("Duplicate number:", find_duplicate(nums))
