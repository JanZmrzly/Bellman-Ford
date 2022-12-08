import csv
import random

def generate_nodes(nodes:int, csv_nodes:type) -> dict:
    header = ['NodeName','NodeID','Neighbours']
    writer = csv.writer(csv_nodes)
    writer.writerow(header)
    graph = {}
    for i in range(nodes):
        node_name = f'{i}'
        node_id = i
        neighbours_cnt = random.randint(0,  5)
        neighbours = []
        
        for _ in range(neighbours_cnt):
            neighbour = random.randint(0, nodes-1)
            
            if neighbour not in neighbours: 
                neighbours.append(neighbour)
        
        writer.writerow([node_name,node_id,neighbours])
        graph[node_id] = neighbours
    
    return graph

def generate_edges(graph:list, nodes:int, csv_edges:type):
    header = ['FromNode','ToNode','NewValue']
    writer = csv.writer(csv_edges)
    writer.writerow(header)
    
    for node_id in range(len(graph)):
        from_node =  node_id
        neighbours = graph[node_id]
        
        for neighbour in neighbours: 
            to_node = neighbour
            new_value = random.randint(0,100)
            writer.writerow([from_node,to_node,new_value])
             
def main(nodes=8):
    nodes = nodes
    csv_nodes = open('nodes.csv', 'w', newline='')
    type(csv_nodes)
    graph = generate_nodes(nodes, csv_nodes)
    csv_nodes.close()

    csv_edges = open('edges.csv', 'w', newline='')
    type(csv_edges)
    generate_edges(graph, nodes, csv_edges)
    csv_edges.close()

if __name__ == '__main__':
    main()