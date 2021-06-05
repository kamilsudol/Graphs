from lib.Project_5.flow_network_representation import FlowNetwork
from lib.Project_5.flow_network_graphics import draw_flow_network
from lib.Project_5.find_maximum_flow import find_maximum_flow

if __name__ == '__main__':
    g = FlowNetwork(3)
    g.generate_random_flow()
    g.setup_capacities(1, 10)

    max_flow = find_maximum_flow(g)
    print("Maxium flow is ", max_flow)

    draw_flow_network(g, draw_capacities=True, draw_flow=True)