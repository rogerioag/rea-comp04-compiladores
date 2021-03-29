from graphviz import Digraph

class Graph:
    class __Node:
        def __init__(self, graph, id, label):
            self.__graph = graph
            self.__id = id
            self.__label = label
            pass

        def id(self):
            return self.__id

        def edge(self, node):
            self.__graph.edge(self, node)
            pass

    def __init__(self, name=None, desc=None):
        self.__name = name
        self.__desc = desc
        self.__dot = Digraph(comment=desc)
        self.__nodes = {}
        pass

    def edge(self, left_node, right_node):
        self.__dot.edge(left_node.id(), right_node.id())
        pass

    def get_node(self, id=None, label=None):
        self.__dot.node(str(id), str(label))
        self.__nodes[id] = Graph.__Node(self, str(id), str(label))
        return self.__nodes[id]

    def export(self, output='graph.gv'):
        self.__dot.render(filename=output)
        pass