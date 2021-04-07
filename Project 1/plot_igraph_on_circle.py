import matplotlib.pyplot as plt
import math


# output fits inside [0, 1] x [0, 1] square
def span_vertices_on_circle(num_of_vertices):
    scaling_factor = 0.5  # bigger => more space outside main, invisible circle and boundaries of region

    vertices = []
    for i in range(num_of_vertices):
        num_of_vertices_clockwise = num_of_vertices - i
        first_vertex_at_the_top_offset = math.pi / 2
        fraction_of_angle = 2 * math.pi / num_of_vertices * num_of_vertices_clockwise + first_vertex_at_the_top_offset
        vertices.append([math.cos(fraction_of_angle) / (2 + scaling_factor) + 0.5,
                         math.sin(fraction_of_angle) / (2 + scaling_factor) + 0.5])

    return vertices


def plot_vertices(vertices, ax):
    circle_radius = 0.04  # 4% of plot width. Maybe make it function of len(vertices)?
    label_from_1 = 1

    for i in range(len(vertices)):
        vertex = plt.Circle((vertices[i][0], vertices[i][1]), circle_radius, color='r', zorder=10)
        ax.add_patch(vertex)
        plt.text(vertices[i][0], vertices[i][1], str(i + label_from_1), ha='center', va='center', fontsize='medium',
                 zorder=11)


def plot_edges(vertices, es):
    for edge in es:
        plt.plot([vertices[edge.source][0], vertices[edge.target][0]],
                 [vertices[edge.source][1], vertices[edge.target][1]])


def normalize_plot(ax):
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    ax.set_aspect('equal')


def plot_igraph_on_circle(g):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(g.vcount())
    plot_vertices(vertices, ax)
    plot_edges(vertices, g.es)

    normalize_plot(ax)
    plt.axis('off')
    plt.show()