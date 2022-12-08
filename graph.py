'''
Autor: Jan Zmrzly
Fakulta strojniho inzenyrstvi VUT v Brne
                              _     _
                             ( \---/ )
                              ) . . (
________________________,--._(___Y___)_,--._______________________ 
                        `--'           `--'      
                    GRAF + Bellman-Ford algoritmus
'''

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from ast import literal_eval
from prettytable import PrettyTable

import time
import csv

'''
Moje objekty, metody a funkce
pro tvorbu grafu
'''

class Node:
    def __init__(self, node_name=None, node_id=None, neighbours=[]):    
        self.node_name = node_name
        self.node_id = node_id
        self.neighbours = neighbours
        self.value = np.inf

    def __str__(self):
        return str({
            'node_name':self.node_name,
            'node_id':self.node_id,
            'neighbours':self.neighbours
        })    

class Graph:
    def __init__(self, nodes_amount):
        self.graph_nodes = {}
        self.edges_values = {}
        self.graph_matrix = np.zeros((nodes_amount,nodes_amount))
        self.graph_matrix_size = 0

    def __str__(self):
        return str(self.graph_nodes)        

    def __repr__(self):
        return self.__str__()

    def add_node(self, node:Node):
        row = []
        column = []
        
        #ulozeni jmena uzlu do slovniku
        self.graph_nodes[node.node_id] = node

        # pokud se s uzlu neda dostat na dalsi, pak neni nutna dalsi iterace
        if node.neighbours == []:
            return
        
        # na zaklade sousedu vepsani 1 do matice sousednosti
        # sestaveni slovniku s hranami a jejich zakladnimi hodnotami 1
        for one_neighbour in node.neighbours:
            self.graph_matrix[node.node_id, one_neighbour] = 1
            self.edges_values[(node.node_id, one_neighbour)] = 1

    def matrix_size(self):
        self.graph_matrix_size = len(self.graph_matrix)

    def change_edge_value(self, edge, new_value):
        if edge not in self.edges_values:
            raise Exception(f'Hodnota hrany nejde zmenit -> hrana {edge} neexistuje')
        
        self.edges_values[edge] = new_value
        self.graph_matrix[edge[0]][edge[1]] = new_value

def bellman_ford(edges_values:dict, graph_nodes:dict, start_node:Node):  
    i = 0
    start_node.value = 0
    list_node_values = []
    list_prev_node_values = []
    current_edges = {}
    removed_edges = {}

    start_time = time.time()
    
    while True:
        current_edges = edges_values
        
        for key in current_edges.keys():

            # zkraceni algoritmu na zaklade Shortest Path Faster Algorithm
            if key in removed_edges.keys():
                continue

            node_id = key[0]
            next_node_id = key[1]

            node = graph_nodes[node_id]
            next_node = graph_nodes[next_node_id]

            # relaxace hlavni cast algoritmu
            new_value = node.value + current_edges[key]
            if new_value < next_node.value:
                next_node.value = new_value
            # zkraceni algoritmu na zaklade Shortest Path Faster Algorithm
            elif new_value == next_node.value:
                for key in current_edges.keys():
                    edge_from_node = key[0]
                    if next_node_id == edge_from_node:
                        removed_edges[key] = current_edges[key]

            list_node_values.append(next_node.value) 

        i += 1

        # ukoncovaci podminky
        # 1) pocet iteraci presehne |v|-1 = nodes
        if i is len(graph_nodes):
            raise Exception(f'Tento graf se nepodarilo vyresit v danem poctu iteraci |v|-1={len(graph_nodes)-1}')
        
        # 2) neni potreba dale iterovat, protoze byla nalezena nejkratsi cesta
        if list_node_values == list_prev_node_values:
            break

        list_prev_node_values = list_node_values
        list_node_values = []
        removed_edges = {}

    print(f'---Time of Execution: {time.time()-start_time}---')

def print_result_table(graph_nodes:dict):
    my_table = PrettyTable()
    list_names = []
    list_ids = []
    list_values = []

    for key in graph_nodes:
        list_names.append(graph_nodes[key].node_name)
        list_values.append(graph_nodes[key].value)
        list_ids.append(graph_nodes[key].node_id)
    
    my_table.add_column('Node(Vertex)', list_names)
    my_table.add_column('Node ID', list_ids)
    my_table.add_column('Distance', list_values)

    print(my_table)

'''
Objekty, metody a funkce knihovny
NetworkX pro tvorbu grafu
Vizualizace grafu

zdroj: https://networkx.org/documentation/stable/index.html

'''

def nx_add_nodes(lib_graph:nx.Graph, node:Node):
    # pridani uzlu
    lib_graph.add_node(node.node_id, node_name=node.node_name, value=node.value)

    # doplneni uzlu na zaklade sousedu
    # pridani hran na zaklade sousedu
    for neighbour in node.neighbours:
        if neighbour not in list(lib_graph.nodes()):
            lib_graph.add_node(neighbour)
        lib_graph.add_edge(node.node_id, neighbour, length=1)

def nx_edge_length(lib_graph:nx.Graph, edge, new_value):
    lib_graph.add_edge(edge[0], edge[1], length=new_value)


'''
                              _     _
                             ( \---/ )
                              ) . . (
________________________,--._(___Y___)_,--._______________________ 
                        `--'           `--' 
                                MAIN

'''

def main():
    # cteni csv souboru, nahrani souboru s definovanymi uzly
    header = []
    rows = []

    file = open('nodes.csv')
    type(file)
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    for row in csvreader: rows.append(row)
    
    # pridani uzlu do vlastniho grafu
    nodes_amount = len(rows)
    my_graph = Graph(nodes_amount)
    my_nodes = []

    for row in rows:
        # nacteni jmena uzlu, id uzlu a sousedu
        node_name = str(row[0])
        node_id = int(row[1])
        neighbours = literal_eval(row[2])
        
        new_node = Node(node_name=node_name, node_id=node_id, neighbours=neighbours)
        my_nodes.append(new_node)
    
    # zavreni souboru
    file.close()

    for node in my_nodes: my_graph.add_node(node)
    # cteni csv souboru, nahrani souboru s definovanymi uzly
    header = []
    rows = []

    file = open('edges.csv')
    type(file)
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    for row in csvreader: rows.append(row)
    
    for row in rows:
        from_node = int(row[0])
        to_node = int(row[1])
        new_value = int(row[2])
        my_graph.change_edge_value(edge=(from_node,to_node), new_value=new_value)

    # hledani nejkratsi cesty pomoci Bellman-Ford algoritmu
    bellman_ford(my_graph.edges_values, my_graph.graph_nodes, my_nodes[0])
    print_result_table(my_graph.graph_nodes)
    
    # vyvoreni paraleniho grafu pomoci knihovny NetworkX
    lib_graph = nx.DiGraph()

    for node in my_nodes: nx_add_nodes(lib_graph, node)
    
    # prepsani hodnot hran v paralenim grafu
    for row in rows:
        from_node = int(row[0])
        to_node = int(row[1])
        new_value = int(row[2])
        nx_edge_length(lib_graph, edge=[from_node,to_node], new_value=new_value)
    
    # zavreni souboru
    file.close()

    # plot graph z knihovny NetworkX, mathplotlib
    labels_edges = nx.get_edge_attributes(lib_graph, 'length')
    labels_nodes_names = nx.get_node_attributes(lib_graph, 'node_name')
    labels_nodes_values = nx.get_node_attributes(lib_graph, 'value')
    pos = nx.kamada_kawai_layout(lib_graph, scale=100)
    
    plt.figure(figsize=(15,8))
    plt.subplot(121).set_title('Zadaný graf')
    nx.draw(lib_graph, pos, labels=labels_nodes_names, with_labels=True, node_size=200, node_color='skyblue', 
            edge_color='#00000F', font_size=8)
    # nx.draw_networkx_edge_labels(lib_graph, pos)
    # nx.draw(lib_graph, pos, labels=labels_nodes_names, with_labels=True, node_size=100)
    # nx.draw_networkx_edge_labels(lib_graph, pos, edge_labels=labels_edges)
    
    plt.subplot(122).set_title('Vzdálenosti uzlů od startu')
    nx.draw(lib_graph, pos, labels=labels_nodes_values, with_labels=True, node_size=200, node_color='skyblue', 
            edge_color='#00000F', font_size=8)
    # nx.draw_networkx_edge_labels(lib_graph, pos)
    # nx.draw(lib_graph, pos, labels=labels_nodes_values, with_labels=True, node_size=100)
    # nx.draw_networkx_edge_labels(lib_graph, pos, edge_labels=labels_edges)
    
    plt.show()
    
if __name__ == '__main__':
    main()

'''
        _____     ____
       /      \  |  o | 
      |        |/ ___\| 
      |_________/     
      |_|_| |_|_|

'''