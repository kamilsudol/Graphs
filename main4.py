from lib.Project_4.random_digraph import digraph_randomizer_start

do_nothing = lambda: None

if __name__ == '__main__':
    exercises = [digraph_randomizer_start, do_nothing]

    while True:
        exercise_index = int(input(
            "Wybierz funkcje:\n - 1 - losuj graf skierowany\n - 2 - zakoncz\n> ").strip()) - 1
        exercises[exercise_index]()
            
        if exercise_index == len(exercises) - 1:
            break

        print()