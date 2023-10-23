'''Hunter Knott, Utah Valley University, CS 2700'''
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

covariate_color = "#2B9BE0"
treatment_color = "#CC5135"
outcome_color = "#4BB846"

matrix = [[0 for i in range(8)] for j in range(8)]

matrix[0][1] = 1 # X -> W3
matrix[1][2] = 1 # W3 -> Y
matrix[3][0] = 1 # W1 -> X
matrix[4][0] = 1 # Z3 -> X
matrix[5][3] = 1 # Z1 -> W1
matrix[5][4] = 1 # Z1 -> Z3
matrix[4][2] = 1 # Z3 -> Y
matrix[6][4] = 1 # Z2 -> Z3
matrix[6][7] = 1 # Z2 -> W2
matrix[7][2] = 1 # W2 -> Y

G = nx.DiGraph()
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            G.add_edge(i, j)

labels = {0: "X", 1: "W3", 2: "Y", 3: "W1", 4: "Z3", 5: "Z1", 6: "Z2", 7: "W2"}
# pos = {0: (-0.7, -0.5), 1: (0, -0.5), 2: (0.7, -0.5), 3: (-0.7, 0), 
#        4: (0, 0), 5: (-0.7, 0.5), 6: (0.7, 0.5), 7: (0.7, 0)}
pos = nx.spring_layout(G, seed=42)
colors = [covariate_color for node in G.nodes]
node_index = list(labels.keys())[list(labels.values()).index("X")]
colors[node_index] = treatment_color
node_index = list(labels.keys())[list(labels.values()).index("Y")]
colors[node_index] = outcome_color

nx.draw_networkx(G, pos=pos, labels=labels, node_color=colors)
plt.show()

def backdoor_criterion(adj_mat, treatment, outcome):
    labels_list = list(labels.values())

    nodes = []
    for i in range(len(matrix)):
        nodes.append(i)
    nodes.remove(nodes[nodes.index(treatment)])
    nodes.remove(nodes[nodes.index(outcome)])
    print(nodes)

    # Find all treatment descendents
    non_admissibles = set()
    i = 0
    for node in matrix[0]:
        if node == 1:
            non_admissibles.add(labels[i])
        i+=1

admissible_sets = backdoor_criterion(matrix, 0, 2)
print(admissible_sets)

# Traverse graph to get all paths
# Take out any path that contains a descendant of the treatment
# Remove one of the covariates in the path, then re-traverse the graph for paths still blocked
# Start node removal with the shortest path, work way up to longer paths