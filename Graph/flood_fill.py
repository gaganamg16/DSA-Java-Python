def flood_fill(image, sr, sc, color):
    original_color = image[sr][sc]

    if original_color == color:
        return image

    def dfs(row, col):
        if row < 0 or row >= len(image):
            return

        if col < 0 or col >= len(image[0]):
            return

        if image[row][col] != original_color:
            return

        image[row][col] = color

        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(sr, sc)

    return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

result = flood_fill(image, 1, 1, 2)

print("Updated image:")

for row in result:
    print(row)