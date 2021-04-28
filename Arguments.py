import argparse


class ArgumentsSingleton():
    __instance = None

    @staticmethod
    def get_instance():
        if ArgumentsSingleton.__instance == None:
            ArgumentsSingleton()
        return ArgumentsSingleton.__instance

    def __init__(self) -> None:
        if ArgumentsSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.ap = argparse.ArgumentParser()
            self.ap.add_argument("-t", "--task", required=False, help="task number", type=int)
            self.ap.add_argument("-f", "--filename", required=False, help="input file name")
            self.ap.add_argument("-o", "--output", required=False, help="graph output format: list/inc/adj")
            self.ap.add_argument("-s", "--shuffles", required=False, help="number of edge randomizations", type=int)
            self.ap.add_argument("-p", "--plots", required=False, help="will it plot? y/n")
            self.arguments = vars(self.ap.parse_args())
            print(self.arguments)
            ArgumentsSingleton.__instance = self 

