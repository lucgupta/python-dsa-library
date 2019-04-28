import sys


class Dijkstra:
    @staticmethod
    def min_distance(dist, vis, n):
        minn = sys.maxsize
        #

        for i in range(n):
            if dist[i] < minn and not vis[i]:
                minn = dist[i]
                min_index = i

        return min_index

    @staticmethod
    def print_graph(dist):

        for i in range(len(dist)):
            print(dist[i], end=' ')

    def find_shortest_dist(self, graph, n):
        # TODO : make dijkstra generic, add src as a parameter.
        maxx = sys.maxsize

        # To record min distance from source
        dist = [maxx for _ in range(n)]
        dist[0] = 0
        vis = [False for _ in range(n)]

        for i in range(n):
            source = self.min_distance(dist, vis, n)
            vis[source] = True

            for i in range(len(graph[source])):
                if graph[source][i] and not vis[i] and dist[source] + graph[source][i] < dist[i]:
                    dist[i] = dist[source] + graph[source][i]

        self.print_graph(dist)


if __name__ == "__main__":
    n = 9

    dijkstra = Dijkstra()

    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
              ]

    dijkstra.find_shortest_dist(graph, n)
