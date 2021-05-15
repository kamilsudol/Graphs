import math


def relax(u, v, distance, previous, adjacency_matrix):
    if distance[v] > distance[u] + adjacency_matrix[u][v]:
        distance[v] = distance[u] + adjacency_matrix[u][v]
        previous[v] = u


def dijkstra_find_shortest_paths(adjacency_matrix, starting_vertex=0):
    n_vertices = len(adjacency_matrix[0])
    previous = [-1] * n_vertices
    distance = [math.inf] * n_vertices
    distance[starting_vertex] = 0
    ready_vertices = []

    while len(ready_vertices) < n_vertices:
        not_calculated_v = [i for i in range(n_vertices) if i not in ready_vertices]
        u = not_calculated_v[0]
        for i in not_calculated_v:
            if distance[i] < distance[u]:
                u = i

        ready_vertices.append(u)
        not_calculated_u_neighbours = [i for i in not_calculated_v if adjacency_matrix[u][i]]
        for v in not_calculated_u_neighbours:
            relax(u, v, distance, previous, adjacency_matrix)

    return distance, previous


def dijkstra_find_and_print_shortest_paths(adjacency_matrix, starting_vertex=0):
    (distance, previous) = dijkstra_find_shortest_paths(adjacency_matrix, starting_vertex)
    print('START: s = {}'.format(starting_vertex + 1))
    for i in range(len(distance)):
        path = []
        k = i
        while k != starting_vertex:
            path.append(k)
            k = previous[k]
        path.append(k)
        path_formatted = list(map(lambda j: j+1, path))[::-1]
        print('distance({}) = {} ==> {}'.format(i + 1, distance[i], path_formatted))


def get_shortest_paths_table(adjacency_matrix):
    res = []
    for i in range(len(adjacency_matrix[0])):
        (d, _) = dijkstra_find_shortest_paths(adjacency_matrix, i)
        res.append(d)
    return res


def print_shortest_paths_table(adjacency_matrix):
    distances = get_shortest_paths_table(adjacency_matrix)
    for row in distances:
        for d in row:
            print('{:<2d} '.format(int(d)), end='')
        print()


def find_graph_center(adjacency_matrix):
    distances = get_shortest_paths_table(adjacency_matrix)
    sums = [sum(row) for row in distances]
    min_val = min(sums)
    return [sums.index(min_val), min_val]


def find_minmax_center(adjacency_matrix):
    distances = get_shortest_paths_table(adjacency_matrix)
    maxes = [max(row) for row in distances]
    min_val = min(maxes)
    return [maxes.index(min_val), min_val]


def print_graph_centers(adjacency_matrix):
    [center, dist_sum] = find_graph_center(adjacency_matrix)
    [minmax_center, max_dist] = find_minmax_center(adjacency_matrix)
    print('Centrum grafu to wezel {} (suma odleglosci: {})'
          .format(center + 1, dist_sum))
    print('Centrum minmax to wezel {} (odleglosc do najdalszego: {})'
          .format(minmax_center + 1, max_dist))
