import matplotlib.pyplot as plt
import math
import numpy as np

from lib.Project_5.flow_network_representation import FlowNetwork

def extract_path(predecessors):
    path = [len(predecessors) - 1]
    prev = predecessors[-1]
    while not math.isnan(prev):
        path.insert(0, int(prev))
        prev = predecessors[int(prev)]
    
    return path

def convert_vertices_path_to_edges(vert_path):
    path = []
    for i in range(len(vert_path) - 1):
        vert = vert_path[i]
        next_vert = vert_path[i+1]
        path.append([vert, next_vert])

    return path

def recreate_path_from_predecessors(predecessors):
    vert_path = extract_path(predecessors)
    return convert_vertices_path_to_edges(vert_path)

def path_from_source_to_target(network: FlowNetwork):
    vertices_count = int(math.pow(network.layers, 2)) + 2
    distances = np.full(vertices_count, float('inf'), float)
    distances[0] = 0
    predecessors = np.full(vertices_count, None, float)
    queue = [0]

    while len(queue):
        v = queue.pop(0)
        for u in range(max(0, v - 2 * network.layers), min(len(network.residual_matrix), v + 2 * network.layers)):
            if network.residual_matrix[v][u] != 0 and distances[u] == float('inf'):
                distances[u] = distances[v] + 1
                predecessors[u] = v
                queue.append(u)

                if u == vertices_count - 1:
                    return recreate_path_from_predecessors(predecessors)
    return None

def path_capacity(network: FlowNetwork, path):
    residuals = network.get_residual_matrix()
    cap = float('inf')
    for i, j in path:
        cap = min(cap, residuals[i][j])

    return cap

def find_maximum_flow(network: FlowNetwork):
    network.set_flows_to_zero()

    path = path_from_source_to_target(network)
    while path is not None:
        path_cap = path_capacity(network, path)

        for i, j in path:
            if network.adj_matrix[i][j] == 1:
                network.flow_matrix[i][j] += path_cap
            else:
                network.flow_matrix[i][j] -= path_cap

        network.update_residual_matrix()
        path = path_from_source_to_target(network)

    return np.sum(network.flow_matrix[0])