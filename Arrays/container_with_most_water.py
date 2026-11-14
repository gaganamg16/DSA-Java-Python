def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])

        area = width * current_height
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("Maximum water:", max_area(height))
