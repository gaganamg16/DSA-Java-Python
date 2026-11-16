def largest_rectangle_area(heights):
    stack = []
    max_area = 0

    for i in range(len(heights) + 1):
        current_height = heights[i] if i < len(heights) else 0

        while stack and current_height < heights[stack[-1]]:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width
            max_area = max(max_area, area)

        stack.append(i)

    return max_area


heights = [2, 1, 5, 6, 2, 3]

print("Largest rectangle area:", largest_rectangle_area(heights))
