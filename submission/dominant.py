import sys
import os
import time
import networkx as nx

avg = 0
count = 0


def is_dominant(g, d):
    # Get all nodes in the graph
    all_nodes = set(g.nodes())

    # Get nodes covered by `d` and their neighbors
    covered_nodes = set(d)
    for node in d:
        covered_nodes.update(g.neighbors(node))

    # Check if all nodes are covered
    return all_nodes == covered_nodes


def find_dominating_set(graph, excluded_nodes):
    dominating_set = set()
    uncovered = set(graph.nodes())

    while uncovered:
        # Find node with maximum uncovered neighbors, respecting exclusions
        best_node = max(
            uncovered,
            key=lambda n: len(set(graph.neighbors(n)) & uncovered)
            if n not in excluded_nodes
            else len(set(graph.neighbors(n)) & uncovered) - 1_000_000,
        )
        dominating_set.add(best_node)
        uncovered -= set(graph.neighbors(best_node)) | {best_node}

    return dominating_set


def best_dominating_pair(D, num_nodes):
    min_score = float("inf")
    best_pair = []

    for i, d1 in enumerate(D):
        for j, d2 in enumerate(D):
            if i < j:  # Ensure each pair is only considered once
                # Calculate score for the pair
                intersection_size = len(d1 & d2)
                score = (len(d1) + len(d2) + intersection_size) / num_nodes

                # Update if a new minimum score is found
                if score < min_score:
                    min_score = score
                    best_pair = (d1, d2)

    intersection_size = len(best_pair[0] & best_pair[1])
    return best_pair, min_score, intersection_size


def dominant(g):
    print("\n\n==== Dominating Sets Information ====")
    global avg, count

    # Calculate two dominating sets
    d1 = find_dominating_set(g, set())
    d2 = find_dominating_set(g, d1)

    # Calculate metrics
    intersection_size = len(d1 & d2)
    score = (len(d1) + len(d2) + intersection_size) / len(g.nodes())

    # Update average score
    count += 1
    avg = (avg * (count - 1) + score) / count

    # Print useful information
    print(f"Number of nodes: {len(g.nodes())}")
    print(f"Number of edges: {len(g.edges())}")
    print(f"Size of d1: {len(d1)}")
    print(f"Size of d2: {len(d2)}")
    print("Is d1 dominant?:", is_dominant(g, d1))
    print("Is d2 dominant?:", is_dominant(g, d2))
    print(f"Intersection size (d1 ∩ d2): {intersection_size}")
    print(f"Score: {score:.4f}")
    print(f"Average Score: {avg:.4f}")
    print(f"Maximal degree of g: {max(g.degree, key=lambda x: x[1])[1]}")

    return list(d1), list(d2)


#########################################
#### Ne pas modifier le code suivant ####
#########################################


def load_graph(name):
    with open(name, "r") as f:
        state = 0
        G = None
        for l in f:
            if state == 0:  # Header nb of nodes
                state = 1
            elif state == 1:  # Nb of nodes
                nodes = int(l)
                state = 2
            elif state == 2:  # Header position
                i = 0
                state = 3
            elif state == 3:  # Position
                i += 1
                if i >= nodes:
                    state = 4
            elif state == 4:  # Header node weight
                i = 0
                state = 5
                G = nx.Graph()
            elif state == 5:  # Node weight
                G.add_node(i, weight=int(l))
                i += 1
                if i >= nodes:
                    state = 6
            elif state == 6:  # Header edge
                i = 0
                state = 7
            elif state == 7:
                if i > nodes:
                    pass
                else:
                    edges = l.strip().split(" ")
                    for j, w in enumerate(edges):
                        w = int(w)
                        if w == 1 and (not i == j):
                            G.add_edge(i, j)
                    i += 1

        return G


#########################################
#### Ne pas modifier le code suivant ####
#########################################
if __name__ == "__main__":
    input_dir = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2])

    # un repertoire des graphes en entree doit être passé en parametre 1
    if not os.path.isdir(input_dir):
        print(input_dir, "doesn't exist")
        exit()

    # un repertoire pour enregistrer les dominants doit être passé en parametre 2
    if not os.path.isdir(output_dir):
        print(input_dir, "doesn't exist")
        exit()

        # fichier des reponses depose dans le output_dir et annote par date/heure
    output_filename = "answers_{}.txt".format(
        time.strftime("%d%b%Y_%H%M%S", time.localtime())
    )
    output_file = open(os.path.join(output_dir, output_filename), "w")

    for graph_filename in sorted(os.listdir(input_dir)):
        # importer le graphe
        g = load_graph(os.path.join(input_dir, graph_filename))

        # calcul du dominant
        d1, d2 = dominant(g)
        D1 = sorted(d1, key=lambda x: int(x))
        D2 = sorted(d2, key=lambda x: int(x))

        # ajout au rapport
        output_file.write(graph_filename)
        for node in D1:
            output_file.write(" {}".format(node))
        output_file.write("-")
        for node in D2:
            output_file.write(" {}".format(node))
        output_file.write("\n")

    output_file.close()
