import numpy as np
import random as rnd
from lib.Project_1.matrix_conversions import adjacency_matrix_to_list
# from lib.Project_1.read_data import print_list


def get_random_w(list):
    n = len(list)
    random_w = []
    while True:
        random_w = np.zeros([n, n], dtype=int)
        sum_w = 0
        for u in range(n):
            for v in list[u]:
                random_w[u][v - 1] = rnd.randint(-5, 10)
        for x in random_w:
            sum_w += sum(x)
        if sum_w > 0: # ochorna przed ujemnym cyklem
            break
    return random_w


def bellman_ford(G, w, s):
    s -= 1
    ds = [np.Inf for v in G]
    ps = [-1 for v in G]
    ds[s] = 0

    for i in range(1, len(G)):
        for u in range(len(G)):
            for v in G[u]:
                if ds[v-1] > ds[u] + w[u][v-1]:
                    ds[v-1] = ds[u] + w[u][v-1]
                    ps[v-1] = u
    for u in range(len(G)):
        for v in G[u]:
            if ds[v - 1] > ds[u] + w[u][v - 1]:
                return False
    print(ds)
    print(ps)
    return True


def test_2_3():
    test = np.array([[0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 1, 0, 0, 1],
                     [0, 1, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 0, 0, 0],
                     [1, 1, 1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0, 1, 0]], dtype=int)

    list = adjacency_matrix_to_list(test)
    random_w = get_random_w(list)
    print(random_w)
    state = bellman_ford(list, random_w, 5)
    print(state)