from anytree import Node, RenderTree
from anytree.exporter import DotExporter

atribuicao = Node("=")
id_a = Node("a", parent=atribuicao)

expressao = Node("+", parent=atribuicao)

id_b = Node("b", parent=expressao)

id_c = Node("c", parent=expressao)

DotExporter(atribuicao).to_picture("atribuicao-asa.png")




