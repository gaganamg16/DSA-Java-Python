nums = [0, 1, 0, 3, 12]

position = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[position], nums[i] = nums[i], nums[position]
        position += 1

print(nums)