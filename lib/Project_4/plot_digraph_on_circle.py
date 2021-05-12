import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import math

from lib.Project_1.TextResizer import *
from lib.Project_1.plot_igraph_on_circle import span_vertices_on_circle, plot_vertices, distance, normalize_plot

from lib.Project_4.weighted_digraph_edges import get_weighed_edges, plot_weighted_edges


def normalize(vec):
    return vec / np.sqrt(np.sum(vec ** 2))


def plot_edges(vertices, es, weights=None):
    for edge in es:
        circle_radius = min(distance(vertices[0], vertices[1]) / 2.3, 0.04)

        parallel = normalize(np.array(vertices[edge.source]) - np.array(vertices[edge.target]))
        perpendicular = normalize(np.array([parallel[1], -parallel[0]]))

        arrowhead_tip = vertices[edge.target] + parallel * circle_radius
        arrowhead_left = arrowhead_tip + normalize(parallel + 0.3 * perpendicular) * circle_radius
        arrowhead_right = arrowhead_tip + normalize(parallel - 0.3 * perpendicular) * circle_radius

        if not edge.is_mutual():
            plot_arr = [arrowhead_left, arrowhead_tip, vertices[edge.source], arrowhead_tip, arrowhead_right]
        else:
            arrowhead_tip2 = vertices[edge.source] - parallel * circle_radius
            arrowhead_left2 = arrowhead_tip2 + normalize(-parallel + 0.3 * perpendicular) * circle_radius
            arrowhead_right2 = arrowhead_tip2 + normalize(-parallel - 0.3 * perpendicular) * circle_radius
            plot_arr = [arrowhead_left, arrowhead_tip, arrowhead_right, arrowhead_tip, arrowhead_tip2, arrowhead_left2,
                        arrowhead_tip2, arrowhead_right2]

        plt.plot([p[0] for p in plot_arr], [p[1] for p in plot_arr])

    if weights is not None:
        plot_weighted_edges(vertices, get_weighed_edges(weights[0], weights[1]))


def plot_digraph_on_circle(g, colormap=None, weights=None):
    fig, ax = plt.subplots()

    vertices = span_vertices_on_circle(g.vcount())
    plot_vertices(vertices, ax, colormap)
    plot_edges(vertices, g.es, weights)

    normalize_plot(ax)
    plt.axis('off')
    plt.show()