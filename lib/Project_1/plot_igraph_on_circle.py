import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import math

from .TextResizer import *

# output fits inside [0, 1] x [0, 1] square
def span_vertices_on_circle(num_of_vertices):
    scaling_factor = 0.2  # bigger => more space outside main, invisible circle and boundaries of region

    vertices = []
    for i in range(num_of_vertices):
        num_of_vertices_clockwise = num_of_vertices - i
        first_vertex_at_the_top_offset = math.pi / 2
        fraction_of_angle = 2 * math.pi / num_of_vertices * num_of_vertices_clockwise + first_vertex_at_the_top_offset
        vertices.append([math.cos(fraction_of_angle) / (2 + scaling_factor) + 0.5,
                         math.sin(fraction_of_angle) / (2 + scaling_factor) + 0.5])

    return vertices


def distance(p1, p2):
    return math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))


def plot_vertices(vertices, ax, colormap):
    circle_radius = min(distance(vertices[0], vertices[1]) / 2.3, 0.04)
    label_from_1 = 1
    if colormap is None:
        colormap = ['r']  * (len(vertices) + 1)

    texts = []
    for i in range(len(vertices)):
        vertex = plt.Circle((vertices[i][0], vertices[i][1]), circle_radius, color=colormap[i + label_from_1], zorder=10)
        ax.add_patch(vertex)

        size = circle_radius * min(ax.bbox.height, ax.bbox.width)
        texts.append(ax.text(vertices[i][0], vertices[i][1], str(i + label_from_1), ha='center', va='center', fontsize=size,
                     color='w', zorder=11))
        texts[-1].set_path_effects([path_effects.Stroke(linewidth=1, foreground='black'), path_effects.Normal()])

    cid = plt.gcf().canvas.mpl_connect("resize_event", TextResizer(texts))


def plot_edges(vertices, es):
    for edge in es:
        plt.plot([vertices[edge.source][0], vertices[edge.target][0]],
                 [vertices[edge.source][1], vertices[edge.target][1]])


def normalize_plot(ax):
    plt.ylim(0, 1)
    plt.xlim(0, 1)
    ax.set_aspect('equal')


def plot_igraph_on_circle(g, colormap=None):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(g.vcount())
    plot_vertices(vertices, ax, colormap)
    plot_edges(vertices, g.es)

    normalize_plot(ax)
    plt.axis('off')
    plt.show()