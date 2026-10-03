nums = [1, 3, 5, 7, 9, 11]
target = 7

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Target found at index:", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Target not found")