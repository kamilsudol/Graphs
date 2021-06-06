from lib.Project_5.flow_network_representation import FlowNetwork
from lib.Project_5.flow_network_graphics import draw_flow_network
from lib.Project_5.find_maximum_flow import find_maximum_flow
from lib.Project_5.Arguments import ArgumentsSingleton
from lib.Utils.decorators import retry_on_value_error

args_singl = ArgumentsSingleton().get_instance()

@retry_on_value_error
def load_layers_count():
    args = args_singl.arguments
    layers_count = args['layers'] if args['layers'] is not None else int(input("Podaj liczbe warstw:\n> "))
    if layers_count < 2:
        raise ValueError("Liczba warstw musi byc wieksza lub rowna od 2")

    return layers_count

if __name__ == '__main__':
    g = FlowNetwork(load_layers_count())
    g.generate_random_flow()
    g.setup_capacities(1, 10)

    max_flow = find_maximum_flow(g)
    print("Masymalny przeplyw to ", max_flow)

    draw_flow_network(g, draw_capacities=True, draw_flow=True)