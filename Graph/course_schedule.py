def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)

    visited = set()
    path = set()

    def dfs(course):
        if course in path:
            return False

        if course in visited:
            return True

        path.add(course)

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        path.remove(course)
        visited.add(course)

        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
