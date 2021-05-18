from lib.Project_1.read_data import load_matrix
from lib.Project_4.digraph_creation import create_digraph_from_adjacency_matrix
from lib.Project_4.plot_digraph_on_circle import plot_digraph_on_circle
import lib.Project_4.random_digraph as rngdi
import lib.Project_2.largest_connected_component as lcc
from lib.Utils.decorators import retry_on_value_error

import numpy as np

time = 0
visited = []
processed = []
component_association = []

def components_recursive(nr, v, graph):
    global component_association
    for u in range(len(graph)):
        if graph[v][u] == 1 and component_association[u] == -1:
            component_association[u] = nr
            components_recursive(nr, u, graph)

def dfs_visit(adj, vertex):
    global time, visited, processed, component_association

    time += 1
    visited[vertex] = time

    for neighbor in range(len(adj)):
        if adj[vertex][neighbor] == 1 and visited[neighbor] == -1:
                dfs_visit(adj, neighbor)

    time += 1
    processed[vertex] = time

def kosaraju(adj):
    global time, visited, processed, component_association

    num_vertices = len(adj)
    visited = [-1] * num_vertices
    processed = [-1] * num_vertices

    time = 0

    for vertex in range(num_vertices):
        if visited[vertex] == -1:
            dfs_visit(adj, vertex)

    transposed = np.transpose(np.array(adj))

    component_association = [-1] * num_vertices
    component_idx = 0

    for _ in range(num_vertices):
        vertex_idx = processed.index(max(processed))
        if component_association[vertex_idx] == -1:
            component_idx += 1
            component_association[vertex_idx] = component_idx
            components_recursive(component_idx, vertex_idx, transposed)

        processed[vertex_idx] = -1

    return component_association

def get_components_vertices(components):
    components_vertex_list = []
    for label in range(1,max(components)+1):
        components_vertex_list.append([])
        for vertex in range(len(components)):
            if label == components[vertex]:
                components_vertex_list[label-1].append(vertex+1)
    
    return components_vertex_list

def test_strongly_connected():
    adj = rngdi.generate_random_digraph()

    #find components with Kosaraju
    print("Szukam składowych...")
    components = kosaraju(adj)

    print("Wynik:")
    components_vertex_list = get_components_vertices(components)
    for l in components_vertex_list:
        print(l)

    colormap = lcc.create_colormap(components_vertex_list)
    plot_digraph_on_circle(create_digraph_from_adjacency_matrix(adj), colormap)