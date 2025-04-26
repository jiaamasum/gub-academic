import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeansManhattan:
    def __init__(self, points, clusters, grid_size=50):
        self.points = points
        self.clusters = clusters
        self.grid_size = grid_size
        self.mat = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.start()

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def start(self):
        
        while True:
            
            for point in self.points:
                min_dist = float('inf')
                for idx, center in enumerate(self.clusters):
                    d = self.manhattan_distance(point, center)
                    if d < min_dist:
                        min_dist = d
                        point.cluster = idx

           
            old_clusters = [Point(c.x, c.y) for c in self.clusters]

            
            for idx in range(len(self.clusters)):
                assigned_points = [p for p in self.points if p.cluster == idx]
                if assigned_points:
                    avg_x = sum(p.x for p in assigned_points) // len(assigned_points)
                    avg_y = sum(p.y for p in assigned_points) // len(assigned_points)
                    self.clusters[idx].x = avg_x
                    self.clusters[idx].y = avg_y

            
            error = sum(
                abs(self.clusters[i].x - old_clusters[i].x) + abs(self.clusters[i].y - old_clusters[i].y)
                for i in range(len(self.clusters))
            )
            if error == 0:
                break

        self.visualize()

    def visualize(self):
        
        for point in self.points:
            self.mat[point.y][point.x] = '*'
        for idx, center in enumerate(self.clusters):
            self.mat[center.y][center.x] = 'C'

        
        for row in self.mat:
            print(' '.join(row))

        print("\nCluster Centers:")
        for idx, center in enumerate(self.clusters):
            print(f"Cluster {idx+1}: ({center.x}, {center.y})")


def generate_data(filename='data.txt', num_points=100, num_clusters=10, grid_size=50):
    points = []
    clusters = []

    with open(filename, 'w') as f:
        f.write("Points:\n")
        for _ in range(num_points):
            x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            points.append(Point(x, y))
            f.write(f"{x} {y}\n")

        f.write("Clusters:\n")
        for _ in range(num_clusters):
            x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            clusters.append(Point(x, y))
            f.write(f"{x} {y}\n")

    return points, clusters


def load_data(filename='data.txt'):
    points = []
    clusters = []
    mode = 'points'

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "Points:":
                mode = 'points'
            elif line == "Clusters:":
                mode = 'clusters'
            elif line:
                x, y = map(int, line.split())
                if mode == 'points':
                    points.append(Point(x, y))
                else:
                    clusters.append(Point(x, y))

    return points, clusters


def main():
    
    points, clusters = generate_data()

    
    kmeans = KMeansManhattan(points, clusters)


if __name__ == "__main__":
    main()
