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
            self.ap.add_argument("-N", "--layers", required=False, help="number of layers between source and target vertices", type=int)
            self.arguments = vars(self.ap.parse_args())
            print(self.arguments)
            ArgumentsSingleton.__instance = self 

