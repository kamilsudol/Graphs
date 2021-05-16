import argparse

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InputArguments(metaclass=Singleton):
    def __init__(self) -> None:
        self.ap = argparse.ArgumentParser()
        self.ap.add_argument("-t", "--task", required=False, help="task number", type=int)
        self.ap.add_argument("-f", "--filename", required=False, help="input file name")
        self.ap.add_argument("-o", "--output", required=False, help="graph output format: list/inc/adj")
        self.ap.add_argument("-s", "--shuffles", required=False, help="number of edge randomizations", type=int)
        self.ap.add_argument("-p", "--plots", required=False, help="will it plot? y/n")
        self.ap.add_argument("-v", "--vertices", required=False, help="number of vertices", type=int)
        self.ap.add_argument("-k", "--regularity", required=False, help="degree of regularity", type=int)
        self.ap.add_argument("-seq", "--sequence", required=False, help="graphic sequence representation")
        self.ap.add_argument("--minv", required=False, help="minimum vertices", type=int)
        self.ap.add_argument("--maxv", required=False, help="maximum vertices", type=int)
        self.args = vars(self.ap.parse_args())
        self.not_none_arguments = dict(filter(lambda item: item[1] is not None, self.args.items()))
        
        if len(self.not_none_arguments) != 0:
            print("Application opened with arguments:")
            for k,v in self.not_none_arguments.items():
                print('{0:12} - {1}'.format(k, v))

    def get_task_number_no_bigger_than(self, maximum_expected):
        if self.args['task'] is not None:
            if 1 <= self.args['task'] <= maximum_expected:
                return self.args['task'];
            
            print(f"Input argument 'task' should be in range [1, {maximum_expected}]")
        
        return None