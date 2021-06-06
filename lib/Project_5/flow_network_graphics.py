import matplotlib.pyplot as plt
from math import atan2, cos, sin
from itertools import product

from lib.Project_5.flow_network_representation import FlowNetwork


def calc_vertex_size(n_layers):
    return 1.0 / (n_layers * 12.0)


def draw_vertex(axes, pos, size, label):
    v = plt.Circle(pos, size, color='steelblue', zorder=3)
    axes.add_patch(v)
    axes.annotate(label, pos, fontsize=400*size, color='white', ha='center', va='center', zorder=3)


def span_vertices(n_layers):
    n = n_layers * n_layers + 2
    layer_spacing = 1.0 / (n_layers + 1)

    v_positions = [[] for _ in range(n + 2)]
    for i in range(n_layers):
        for j in range(n_layers):
            v_positions[i * n_layers + j + 1] = [(i + 1) * layer_spacing, (j + 1) * layer_spacing]

    v_positions[0] = [0.0, 0.5]
    v_positions[n-1] = [1.0, 0.5]
    return v_positions


def draw_vertices(axes, layers, positions):
    n_layers = len(layers) - 2
    vertex_size = calc_vertex_size(len(layers) - 2)

    n = n_layers * n_layers + 2
    for i in range(n):
        draw_vertex(axes=axes, pos=positions[i], size=vertex_size, label=i)


def arrow_between_vertices(v1, v2, vertex_size, text, color='coral'):
    dx = v2[0] - v1[0]
    dy = v2[1] - v1[1]
    angle = atan2(dy, dx)
    corr_x = vertex_size * cos(angle)
    corr_y = vertex_size * sin(angle)
    dx -= corr_x
    dy -= corr_y
    plt.arrow(v1[0], v1[1], dx, dy, color=color, linewidth=0, width=0.005, length_includes_head=True)
    if text:
        plt.annotate(text, (v1[0] + 0.3 * dx, v1[1] + 0.3 * dy))


def draw_connections(network: FlowNetwork, vertex_positions, draw_capacities=True, draw_flow=True):
    capacities = network.get_capacity_matrix()
    flow = network.get_flow_matrix()
    vertex_size = calc_vertex_size(network.layers)
    for i, j in product(range(len(capacities)), repeat = 2):
        if network.is_edge_in_network(i, j):
            text = ''
            if draw_capacities and draw_flow:
                text = '[{}/{}]'.format(int(flow[i][j]), int(capacities[i][j]))
            elif draw_capacities:
                text = '[{}]'.format(int(capacities[i][j]))
            color = 'yellowgreen' if flow[i][j] == 0 else 'red' if flow[i][j] == capacities[i][j] else 'coral'
            arrow_between_vertices(vertex_positions[i], vertex_positions[j], vertex_size, text=text, color=color)


def draw_flow_network(network: FlowNetwork, draw_capacities=False, draw_flow=False):
    n_layers = network.layers
    layers = [[] for _ in range(n_layers + 2)]
    layers[0] = [0]
    for k in range(n_layers):
        layers[k+1] = [n_layers * k + i for i in range(1, n_layers + 1)]
    layers[n_layers+1] = [n_layers * n_layers + 1]

    figure, axes = plt.subplots()
    axes.set_aspect('equal')
    plt.axis('off')
    plt.margins(0.05)

    positions = span_vertices(n_layers)
    draw_vertices(axes, layers, positions)
    draw_connections(network, positions, draw_capacities, draw_flow)

    plt.show()
