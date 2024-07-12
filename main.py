# This is a Python script example using A* Informed Search

from collections import deque


class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            '46th_Vanderbilt': 1,
            '45th_Vanderbilt': 1,
            '44th_Vanderbilt': 1,
            '43rd_Vanderbilt': 1,
            '42nd_Vanderbilt': 1,
            '46th_Madison': 1,
            '45th_Madison': 1,
            '44th_Madison': 1,
            '43rd_Madison': 1,
            '42nd_Madison': 1,
            '41st_Madison': 1,
            '40th_Madison': 1,
            '39th_Madison': 1,
            '45th_5th': 1,
            '44th_5th': 1,
            '43rd_5th': 1,
            '42nd_5th': 1,
            '41st_5th': 1,
            '40th_5th': 1,
            '39th_5th': 1,
            '43rd_Americas': 1,
            '42nd_Americas': 1,
            '41st_Americas': 1,
            '40th_Americas': 1,
            '39th_Americas': 1,
            '41st_Broadway': 1,
            '40th_Broadway': 1
        }

        return H[n]

        # heuristic function for all nodes when time between 2pm and 7pm
    def hLate(self, n):
        H = {
            '46th_Vanderbilt': 1,
            '45th_Vanderbilt': 1,
            '44th_Vanderbilt': 1,
            '43rd_Vanderbilt': 1,
            '42nd_Vanderbilt': 4,
            '46th_Madison': 1,
            '45th_Madison': 1,
            '44th_Madison': 1,
            '43rd_Madison': 1,
            '42nd_Madison': 4,
            '41st_Madison': 1,
            '40th_Madison': 1,
            '39th_Madison': 6,
            '45th_5th': 4,
            '44th_5th': 4,
            '43rd_5th': 4,
            '42nd_5th': 4,
            '41st_5th': 4,
            '40th_5th': 4,
            '39th_5th': 6,
            '43rd_Americas': 1,
            '42nd_Americas': 4,
            '41st_Americas': 1,
            '40th_Americas': 1,
            '39th_Americas': 6,
            '41st_Broadway': 1,
            '40th_Broadway': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node, late_time):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            if late_time.lower() == 'yes'.lower():
                for v in open_list:
                    if n == None or g[v] + self.hLate(v) < g[n] + self.hLate(n):
                        n = v;
            else:
                for v in open_list:
                    if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                        n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructing the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


adjacency_list = {
    '46th_Vanderbilt': [('45th_Vanderbilt', 1), ('44th_Vanderbilt', 2), ('43rd_Vanderbilt', 3), ('42nd_Vanderbilt', 4)],
    '45th_Vanderbilt': [('44th_Vanderbilt', 1), ('43rd_Vanderbilt', 2), ('42nd_Vanderbilt', 3), ('45th_Madison', 1),
                        ('45th_5th', 3)],
    '44th_Vanderbilt': [('43rd_Vanderbilt', 1), ('42nd_Vanderbilt', 2)],
    '43rd_Vanderbilt': [('42nd_Vanderbilt', 1), ('43rd_Madison', 1), ('43rd_5th', 3), ('43rd_Americas', 6)],
    '42nd_Vanderbilt': [('42nd_Madison', 1), ('42nd_5th', 3), ('42nd_Americas', 6)],
    '46th_Madison': [('46th_Vanderbilt', 1)],
    '45th_Madison': [('46th_Madison', 1), ('45th_5th', 2)],
    '44th_Madison': [('45th_Madison', 1), ('46th_Madison', 2), ('44th_Vanderbilt', 1)],
    '43rd_Madison': [('44th_Madison', 1), ('45th_Madison', 2), ('46th_Madison', 3), ('43rd_5th', 2),
                     ('43rd_Americas', 5)],
    '42nd_Madison': [('43rd_Madison', 1), ('44th_Madison', 2), ('45th_Madison', 3), ('46th_Madison', 4),
                     ('42nd_5th', 2),
                     ('42nd_Americas', 5)],
    '41st_Madison': [('42nd_Madison', 1), ('43rd_Madison', 2), ('44th_Madison', 3), ('45th_Madison', 4),
                     ('46th_Madison', 5)],
    '40th_Madison': [('41st_Madison', 1), ('42nd_Madison', 2), ('43rd_Madison', 3), ('44th_Madison', 4),
                     ('45th_Madison', 5),
                     ('46th_Madison', 6)],
    '39th_Madison': [('40th_Madison', 1), ('41st_Madison', 2), ('42nd_Madison', 3), ('43rd_Madison', 4),
                     ('44th_Madison', 5),
                     ('45th_Madison', 6), ('46th_Madison', 7), ('39th_5th', 2), ('39th_Americas', 5)],
    '45th_5th': [('44th_5th', 1), ('43rd_5th', 2), ('42nd_5th', 3), ('41st_5th', 4), ('40th_5th', 5), ('39th_5th', 6)],
    '44th_5th': [('43rd_5th', 1), ('42nd_5th', 2), ('41st_5th', 3), ('40th_5th', 4), ('39th_5th', 5),
                 ('44th_Madison', 2),
                 ('44th_Vanderbilt', 3)],
    '43rd_5th': [('42nd_5th', 1), ('41st_5th', 2), ('40th_5th', 3), ('39th_5th', 4), ('43rd_Americas', 3)],
    '42nd_5th': [('41st_5th', 1), ('40th_5th', 2), ('39th_5th', 3), ('42nd_Americas', 3)],
    '41st_5th': [('40th_5th', 1), ('39th_5th', 2), ('41st_Madison', 2)],
    '40th_5th': [('39th_5th', 1), ('40th_Madison', 2)],
    '39th_5th': [('39th_Americas', 3)],
    '43rd_Americas': [],
    '42nd_Americas': [('43rd_Americas', 1)],
    '41st_Americas': [('42nd_Americas', 1), ('43rd_Americas', 2), ('41st_Broadway', 2)],
    '40th_Americas': [('41st_Americas', 1), ('42nd_Americas', 2), ('43rd_Americas', 3)],
    '39th_Americas': [('40th_Americas', 1), ('41st_Americas', 2), ('42nd_Americas', 3), ('43rd_Americas', 4)],
    '41st_Broadway': [('40th_Broadway', 1)],
    '40th_Broadway': [('40th_Americas', 2)]
}

lateTime = input("Is it currently between 2 and 7pm? ")
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('45th_Vanderbilt', '39th_Americas', lateTime)
