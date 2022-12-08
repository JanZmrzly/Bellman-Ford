from generate_graph import main as generator
from graph import main as run_graph

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--nodes', type=int, help='Insert amount of nodes in your graph')
    args = parser.parse_args()
    
    if args.nodes is None:
        raise Exception('Nebyl vlozen pocet uzlu')
    
    generator(args.nodes)
    run_graph()

if __name__ == '__main__':
    main()