from enum import Enum
from .igraph_creation import *
from .matrix_conversions import *


class MatrixRepresentation(Enum):
    List = 0
    IncidenceMatrix = 1
    AdjacencyMatrix = 2
    UndeterminedMatrix = 3

    @staticmethod
    def string_dict():
        return {
            MatrixRepresentation.List: "lista sasiedztwa",
            MatrixRepresentation.IncidenceMatrix: "macierz incydencji",
            MatrixRepresentation.AdjacencyMatrix: "macierz sasiedztwa",
            MatrixRepresentation.UndeterminedMatrix: "macierz sasiedztwa i incydencji"
        }

    def to_string(self):
        return MatrixRepresentation.string_dict().get(self)

    @staticmethod
    def create_igraph_func_dict():
        return {
            MatrixRepresentation.List: create_igraph_from_list,
            MatrixRepresentation.IncidenceMatrix: create_igraph_from_incidence_matrix,
            MatrixRepresentation.AdjacencyMatrix: create_igraph_from_adjacency_matrix,
            MatrixRepresentation.UndeterminedMatrix: create_igraph_from_adjacency_matrix
        }

    def to_igraph_func(self):
        return MatrixRepresentation.create_igraph_func_dict().get(self)

    @staticmethod
    def convert_func_dict():
        return {
            MatrixRepresentation.IncidenceMatrix.name + MatrixRepresentation.List.name: incidence_matrix_to_list,
            MatrixRepresentation.List.name + MatrixRepresentation.IncidenceMatrix.name: list_to_incidence_matrix,
            MatrixRepresentation.AdjacencyMatrix.name + MatrixRepresentation.List.name: adjacency_matrix_to_list,
            MatrixRepresentation.List.name + MatrixRepresentation.AdjacencyMatrix.name: list_to_adjacency_matrix,
            MatrixRepresentation.AdjacencyMatrix.name + MatrixRepresentation.IncidenceMatrix.name: adjacency_matrix_to_incidence_matrix,
            MatrixRepresentation.IncidenceMatrix.name + MatrixRepresentation.AdjacencyMatrix.name: incidence_matrix_to_adjacency_matrix
        }

    def convert_func(self, to):
        if self == to:
            return lambda matrix: matrix

        return MatrixRepresentation.convert_func_dict().get(self.name + to.name)
