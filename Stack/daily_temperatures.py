def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print("Days to wait:", daily_temperatures(temperatures))
