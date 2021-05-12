from lib.Project_1.igraph_creation import create_igraph_from_adjacency_matrix
from lib.Project_1.plot_igraph_on_circle import plot_igraph_on_circle
from lib.Project_1.read_data import load_matrix

import numpy as np
import numpy.lib.recfunctions as recfunctions


def load_sequence(sequence_input=None):
    if sequence_input is None:
        sequence_input = input('Wprowadz ciag: ').strip().split(' ')
    else:
        sequence_input = sequence_input.strip().split(' ')
    return [int(i) for i in sequence_input]


def is_graphic_sequence(seq):
    seq = np.sort(seq)[::-1]
    seq = recfunctions.merge_arrays([seq, range(len(seq))])
    seq.dtype.names = ['neighbors', 'vertex']
    adj_matrix = np.zeros((len(seq), len(seq)))

    while True:
        if np.all(seq['neighbors'] == 0):
            return adj_matrix

        if seq[0]['neighbors'] >= len(seq) or np.any(seq['neighbors'] < 0) or np.count_nonzero(seq['neighbors'] % 2 == 1) % 2 == 1:
            return False

        for i in range(1, seq[0]['neighbors'] + 1):
            seq[i]['neighbors'] -= 1
            adj_matrix[ seq[0]['vertex'] ][ seq[i]['vertex'] ] = adj_matrix[ seq[i]['vertex'] ][ seq[0]['vertex'] ] = 1

        seq[0]['neighbors'] = 0
        seq.sort(order='neighbors')
        seq = seq[::-1]


def test_graphic_sequence(filename=None, seq=None, plot=None):
    if filename is not None and seq is not None:
        print("Wprowadzono za duzo argumentow!")
        raise ValueError
    else:
        if filename is None:
            seq = load_sequence(seq)
        else:
            seq = load_matrix(filename)[0]

    res = is_graphic_sequence(seq)

    if res is not False:
        print("Ciag jest graficzny")
        graph = create_igraph_from_adjacency_matrix(res)
        if plot is None or plot == 'y':
            plot_igraph_on_circle(graph)
    else:
        print("Ciag nie jest graficzny")