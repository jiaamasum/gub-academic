def is_valid(graph, color, c, node):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def coloring(graph, color, k, node, n):
    if node == n:
        return True
    for c in range(1, k+1):
        if is_valid(graph, color, c, node):
            color[node] = c
            if coloring(graph, color, k, node+1, n):
                return True
            color[node] = 0
    return False

def getting_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    n, m, k = map(int, lines[0].split())
    graph = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v = map(int, line.strip().split())
        graph[u].append(v)
        graph[v].append(u)
    return n, k, graph


def solve(file_path):
    n, k, graph = getting_input(file_path)
    color = [0] * n

    if coloring(graph, color, k, 0, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {k} Colors")


if __name__ == "__main__":
    file_path = input("Enter input file path: ")
    solve(file_path)
