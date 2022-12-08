import numpy as np

class Node:
    def __init__(self, value, node_id):
        self.value = value
        self.node_id = node_id

def bellman_ford(dic_edges:dict, dic_nodes:dict, start_node):  
    i = 0
    start_node.value = 0
    list_node_values = []
    list_prev_node_values = []

    while True:
        for key in dic_edges.keys():
            node_id = key[0]
            next_node_id = key[1]

            node = dic_nodes[node_id]
            next_node = dic_nodes[next_node_id]

            # relaxace hlavni cast algoritmu
            new_value = node.value + dic_edges[key]
            if new_value < next_node.value:
                next_node.value = new_value
            
            list_node_values.append(next_node.value) 

        i += 1

        # ukoncovaci podminky
        # 1) pocet iteraci presehne |v|-1 = nodes
        if i is len(dic_nodes):
            raise Exception(f'Tento graf se nepodarilo vyresit v danem poctu iteraci |v|-1={len(dic_nodes)-1}')
        
        # 2) neni potreba dale iterovat, protoze byla nalezena nejkratsi cesta
        if list_node_values == list_prev_node_values:
            break

        list_prev_node_values = list_node_values
        list_node_values = []

def main():  
    # slovnik obasuhijici hrany
    dic_edge = {}   
    dic_edge[(0,1)] = 6
    dic_edge[(0,2)] = 5
    dic_edge[(0,3)] = 5
    dic_edge[(2,1)] = -2
    dic_edge[(3,2)] = -2
    dic_edge[(2,4)] = 1
    dic_edge[(1,4)] = -1
    dic_edge[(3,5)] = -1
    dic_edge[(5,6)] = 3
    dic_edge[(4,6)] = 3

    graph_matrix = np.zeros((7,7))
    graph_matrix[0][1] = 6
    graph_matrix[0][2] = 5
    graph_matrix[0][3] = 5
    graph_matrix[2][1] = -2
    graph_matrix[3][2] = -2
    graph_matrix[2][4] = 1
    graph_matrix[1][4] = -1
    graph_matrix[3][5] = -1
    graph_matrix[5][6] = 3
    graph_matrix[4][6] = 3

    A = Node(0, 0)
    B = Node(np.inf, 1)
    C = Node(np.inf, 2)
    D = Node(np.inf, 3)
    E = Node(np.inf, 4)
    F = Node(np.inf, 5)
    G = Node(np.inf, 6)

    dic_node = {}
    dic_node[0] = A
    dic_node[1] = B
    dic_node[2] = C
    dic_node[3] = D
    dic_node[4] = E
    dic_node[5] = F
    dic_node[6] = G

    bellman_ford(dic_edge, dic_node)

    for key in dic_node:
        print(key, dic_node[key].value)

if __name__ == '__main__':
    main()