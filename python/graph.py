import networkx as nx
import pprint
from calc_distances import distance_meters


def main():
    G = nx.Graph()

    with open('coords.txt', 'r') as fin:
        for line in fin:
            line = line.split()
            label = int(line[0])
            lat = float(line[1])
            long = float(line[2])
            G.add_node(label)
            G.node[label]['lat'] = lat
            G.node[label]['long'] = long

    G.add_weighted_edges_from([(6, 7, distance_meters(G.node[6], G.node[7])),
                               (7, 8, distance_meters(G.node[7], G.node[8])),
                               (7, 9, distance_meters(G.node[7], G.node[9])),
                               (8, 13, distance_meters(G.node[8], G.node[13])),
                               (13, 14, distance_meters(G.node[13], G.node[14])),
                               (13, 22, distance_meters(G.node[13], G.node[22])),
                               (22, 26, distance_meters(G.node[22], G.node[26])),
                               (22, 21, distance_meters(G.node[22], G.node[21])),
                               (26, 27, distance_meters(G.node[26], G.node[27])),
                               (27, 28, distance_meters(G.node[27], G.node[28])),
                               (28, 29, distance_meters(G.node[28], G.node[29])),
                               (29, 30, distance_meters(G.node[29], G.node[30])),
                               (29, 25, distance_meters(G.node[29], G.node[25])),
                               (14, 12, distance_meters(G.node[14], G.node[12])),
                               (14, 21, distance_meters(G.node[14], G.node[21])),
                               (14, 20, distance_meters(G.node[14], G.node[20])),
                               (12, 9, distance_meters(G.node[12], G.node[9])),
                               (12, 19, distance_meters(G.node[12], G.node[19])),
                               (20, 19, distance_meters(G.node[20], G.node[19])),
                               (20, 24, distance_meters(G.node[20], G.node[24])),
                               (20, 23, distance_meters(G.node[20], G.node[23])),
                               (23, 21, distance_meters(G.node[23], G.node[21])),
                               (23, 25, distance_meters(G.node[23], G.node[25])),
                               (25, 24, distance_meters(G.node[25], G.node[24])),
                               (19, 24, distance_meters(G.node[19], G.node[24])),
                               (19, 18, distance_meters(G.node[19], G.node[18])),
                               (18, 17, distance_meters(G.node[18], G.node[17])),
                               (18, 15, distance_meters(G.node[18], G.node[15])),
                               (17, 15, distance_meters(G.node[17], G.node[15])),
                               (11, 15, distance_meters(G.node[11], G.node[15])),
                               (11, 16, distance_meters(G.node[11], G.node[16])),
                               (17, 16, distance_meters(G.node[17], G.node[16])),
                               (11, 10, distance_meters(G.node[11], G.node[10])),
                               (11, 9, distance_meters(G.node[11], G.node[9])),
                               (17, 3, distance_meters(G.node[17], G.node[3])),
                               (2, 3, distance_meters(G.node[2], G.node[3])),
                               (4, 3, distance_meters(G.node[4], G.node[3])),
                               (4, 5, distance_meters(G.node[4], G.node[5])),
                               (1, 5, distance_meters(G.node[1], G.node[5])),
                               (1, 31, distance_meters(G.node[1], G.node[31])),
                               (30, 31, distance_meters(G.node[30], G.node[31])),
                               (2, 31, distance_meters(G.node[2], G.node[31])),
                               (2, 24, distance_meters(G.node[2], G.node[24]))])

    print('mwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmw\n'
          '       Adjacency Information:\n'
          'wmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwm')
    for edge in G.adjacency():
        pprint.pprint(edge)
    print()

    # For use as heuristic distances in A*
    # To lookup distance between two nodes x and y, use
    #           dist_matrix[x][y]
    dist_matrix = dict()
    for source_node in G.nodes():
        dist_matrix[source_node] = dict()
        for target_node in G.nodes():
            if source_node is target_node:
                dist_matrix[source_node][target_node] = 0.0
            else:
                dist_matrix[source_node][target_node] = distance_meters(G.node[source_node], G.node[target_node])

    print('mwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmw\n'
          '       Sample A* paths:\n'
          'wmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwmwm')
    print('A* (12, 5): ', nx.astar_path(G, 12, 5))
    print('     length = ', nx.astar_path_length(G, 12, 5), '\n')
    print('A* (4, 23): ', nx.astar_path(G, 4, 23))
    print('     length = ', nx.astar_path_length(G, 4, 23), '\n')
    print('A* (4, 24): ', nx.astar_path(G, 4, 24))
    print('     length = ', nx.astar_path_length(G, 4, 24), '\n')
    print('A* (26, 15): ', nx.astar_path(G, 26, 15))
    print('     length = ', nx.astar_path_length(G, 12, 5), '\n')
    print('A* (9, 1): ', nx.astar_path(G, 9, 1))
    print('     length = ', nx.astar_path_length(G, 9, 1), '\n')
    print('A* (12, 25): ', nx.astar_path(G, 12, 25))
    print('     length = ', nx.astar_path_length(G, 12, 25), '\n')

if __name__ == '__main__':
    main()
