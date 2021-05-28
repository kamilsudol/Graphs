import numpy as np
import random
from lib.Project_4.plot_digraph_on_circle import plot_digraph_on_circle
from lib.Project_4.DiMatrixRepresentation import DiMatrixRepresentation


class FlowNetwork:
    def __init__(self, N):
        self.nodes = N * N
        self.layers = N
        self.size = self.nodes + 2
        self.flow_matrix = np.zeros([self.size, self.size], dtype=int)
        self.initial_state()

    def initial_state(self):
        for i in range(self.layers):
            self.flow_matrix[0][i + 1] = 1
            self.flow_matrix[self.layers * i + 1][self.layers * (i + 1) + 1] = 1
            self.flow_matrix[self.nodes - i][self.nodes + 1] = 1

    def test_print(self):
        graph_plot = DiMatrixRepresentation.AdjacencyMatrix.to_digraph_func()(self.flow_matrix)
        plot_digraph_on_circle(graph_plot)
        print(self.flow_matrix)

    def get_flow_matrix(self):
        return self.flow_matrix

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

                if flag is False:
                    break

    def __generate_random_flow_on_layers(self, min, max) -> (bool):
        node_choice_x = random.randrange(min, max)
        node_choice_y = random.randrange(min, max)

        if abs(node_choice_x - node_choice_y) >= self.layers:
            return True

        if node_choice_x == node_choice_y or self.flow_matrix[node_choice_y][node_choice_x] == 1:
            return True
        else:
            self.flow_matrix[node_choice_y][node_choice_x] = 1
            return False
