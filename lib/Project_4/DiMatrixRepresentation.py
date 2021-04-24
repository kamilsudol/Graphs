from enum import Enum
from .digraph_creation import *


class DiMatrixRepresentation(Enum):
    List = 0
    IncidenceMatrix = 1
    AdjacencyMatrix = 2
    UndeterminedMatrix = 3

    @staticmethod
    def string_dict():
        return {
            DiMatrixRepresentation.List: "lista sasiedztwa",
            DiMatrixRepresentation.IncidenceMatrix: "macierz incydencji",
            DiMatrixRepresentation.AdjacencyMatrix: "macierz sasiedztwa",
            DiMatrixRepresentation.UndeterminedMatrix: "macierz sasiedztwa i incydencji"
        }

    def to_string(self):
        return DiMatrixRepresentation.string_dict().get(self)

    @staticmethod
    def create_digraph_func_dict():
        return {
            #DiMatrixRepresentation.List: create_digraph_from_list,
            #DiMatrixRepresentation.IncidenceMatrix: create_digraph_from_incidence_matrix,
            DiMatrixRepresentation.AdjacencyMatrix: create_digraph_from_adjacency_matrix
            #DiMatrixRepresentation.UndeterminedMatrix: create_digraph_from_adjacency_matrix
        }

    def to_digraph_func(self):
        return DiMatrixRepresentation.create_digraph_func_dict().get(self)
