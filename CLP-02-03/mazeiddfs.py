def iddfs(maze, start, target):
    rows, cols = len(maze), len(maze[0])
    dir = [(-1,0), (1,0), (0,-1), (0,1)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    def dls(x, y, depth, limit, visited, path):
        if (x, y) == target:
            path.append((x, y))
            return True
        if depth >= limit:
            return False

        visited.add((x, y))
        path.append((x, y))

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                if dls(nx, ny, depth + 1, limit, visited, path):
                    return True

        path.pop()
        visited.remove((x, y))
        return False

    depth_search = rows * cols
    for depth in range(depth_search + 1):
        visited = set()
        path = []
        if dls(start[0], start[1], 0, depth, visited, path):
            return True, depth, path
    return False, depth_search, []

if __name__ == "__main__":
    rows, cols = map(int, input("Enter row and column in digits(give space): ").split())
    print("Enter the rows(give space):")
    maze = [list(map(int, input().split())) for _ in range(rows)]

    sx, sy = map(int, input("Enter Start (x y): ").split())
    tx, ty = map(int, input("Enter Target (x y): ").split())

    found, depth, path = iddfs(maze, (sx, sy), (tx, ty))

    if found:
        print(f"\nPath found at {depth} using IDDFS")
        print("Traversal Order:", path)
    else:
        print(f"\nPath not found  at {depth} using IDDFS")
