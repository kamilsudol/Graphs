import numpy as np
import random
import lib.Project_3.random_weighted_graph as rngraph_wei
from lib.Project_4.plot_digraph_on_circle import plot_digraph_on_circle
from lib.Project_4.digraph_creation import create_digraph_from_adjacency_matrix


class FlowNetwork:
    def __init__(self, N):
        self.nodes = N * N
        self.layers = N
        self.size = self.nodes + 2
        self.adj_matrix = np.zeros([self.size, self.size], dtype=int)
        self.flow_matrix = np.zeros_like(self.adj_matrix)
        self.capacity_matrix = np.zeros_like(self.adj_matrix)
        self.residual_matrix = np.zeros_like(self.adj_matrix)
        self.initial_state()

    def initial_state(self):
        try:
            for i in range(self.layers):
                self.adj_matrix[0][i + 1] = 1
                self.adj_matrix[self.nodes - i][self.nodes + 1] = 1
                for j in range(self.layers):
                    self.adj_matrix[self.layers * i + j + 1][self.layers * (i + 1) + j + 1] = 1
        except IndexError:
            pass

    def get_adj_matrix(self):
        return self.adj_matrix

    def get_flow_matrix(self):
        return self.flow_matrix

    def get_capacity_matrix(self):
        return self.capacity_matrix

    def get_residual_matrix(self):
        return self.residual_matrix

    def set_flows_to_zero(self):
        self.flow_matrix = np.zeros_like(self.flow_matrix)
        self.update_residual_matrix()

    def generate_random_flow(self):
        for x in range(2 * self.layers):
            while True:
                layer_choice = random.randrange(self.layers)
                if layer_choice == 0:
                    flag = self.__generate_random_flow_on_layers(1, 2 * self.layers + 1)
                elif layer_choice == self.layers - 1:
                    flag = self.__generate_random_flow_on_layers(self.nodes - 2 * self.layers + 1,
                                                                 self.nodes + 1)
                else:
                    flag = self.__generate_random_flow_on_layers(self.layers * layer_choice + 1 - self.layers,
                                                                 self.layers * layer_choice + 2 * self.layers + 1)

                if flag is True:
                    break

    def __generate_random_flow_on_layers(self, min, max) -> (bool):
        node_choice_x = random.randrange(min, max)
        node_choice_y = random.randrange(min, max)

        if node_choice_x == node_choice_y:
            return False

        if abs(np.ceil(node_choice_x / self.layers) - np.ceil(node_choice_y / self.layers)) > 1:
            return False

        if self.adj_matrix[node_choice_x][node_choice_y] == 1 or self.adj_matrix[node_choice_y][node_choice_x] == 1:
            return False
        else:
            self.adj_matrix[node_choice_y][node_choice_x] = 1
            return True

    def setup_capacities(self, min_capacity, max_capacity):
        self.capacity_matrix = rngraph_wei.assign_weights_to_graph(self.get_adj_matrix(), min_capacity, max_capacity)
        self.update_residual_matrix()

    def residual_capacity(self, i, j):
        if self.adj_matrix[i][j] == 1:
            return self.capacity_matrix[i][j] - self.flow_matrix[i][j]
        elif self.adj_matrix[j][i] == 1:
            return self.flow_matrix[j][i]
        else:
            return 0

    def update_residual_matrix(self):
        for i in range(len(self.residual_matrix)):
            for j in range(len(self.residual_matrix[0])):
                self.residual_matrix[i][j] = self.residual_capacity(i, j)