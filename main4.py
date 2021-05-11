from lib.Project_4.random_digraph import digraph_randomizer_start
from lib.Project_4.strongly_connected_component import test_strongly_connected
from lib.Project_4.bellman_ford import test_2_3
from lib.Utils.decorators import retry_on_value_error


@retry_on_value_error
def get_exercise_index():
    index = int(input(
        "Wybierz funkcje:\n"
        " - 1 - losuj graf skierowany\n"
        " - 2 - znajdz najwieksza silnie spojna skladowa\n"
        " - 3 - znajdz najkrotsza sciezke do danego wierzcholka\n"
        " - 4 - \n"
        " - 5 - zakoncz\n> ").strip()) - 1

    if index < 0 or index > 4:
        raise ValueError 

    return index

do_nothing = lambda: None

if __name__ == '__main__':
    exercises = [digraph_randomizer_start, test_strongly_connected, test_2_3, do_nothing]

    while True:
        exercise_index = get_exercise_index()
        if exercise_index == len(exercises):
            break

        retry_on_value_error(
            lambda : exercises[exercise_index]()
        )()

        print()