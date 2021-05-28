from lib.Project_5.flow_network_representation import FlowNetwork

if __name__ == '__main__':
    g = FlowNetwork(3)
    g.generate_random_flow()
    g.test_print()