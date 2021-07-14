

class TreeNode:
    INCREMENT = 0
    def __init__(self, id=None, raw=None):
        self.__nodes = []
        self.__id = id
        self.__raw = raw
        self.__increment = TreeNode.INCREMENT

        TreeNode.INCREMENT += 1
        pass

    def __str__(self):
        if self.__id and self.__raw:
            return f'{self.__id} \'{self.__raw}\''
        elif self.__id:
            return f'{self.__id}'
        else:
            return f'{self.__raw}'

    def __repr__(self):
        return str(self)

    def nodes(self):
        return self.__nodes

    def insert_nodes(self, nodes):
        self.__nodes.extend(nodes)
        pass

    def insert_node(self, node):
        self.__nodes.append(node)

        return len(self.__nodes)

    def insert_node_with_child(self, father, child):
        father.__nodes.append(child)
        return self.insert_node(father)

    def render(self, graph):

        node = graph.get_node(id=self.__increment, label=str(self))

        for sub in self.__nodes:
            node.edge(sub.render(graph))
            pass

        return node
    pass