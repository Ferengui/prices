# Reimportando as bibliotecas e recriando o Diagrama de Objeto UML
from graphviz import Digraph

# Recriando o diagrama de objeto com uma organização melhor
refined_object_diagram = Digraph(comment='Diagrama de Objeto - Comparador de Preços (Refinado)', format='png')
refined_object_diagram.attr(rankdir='TB', fontsize='10')
refined_object_diagram.attr('node', shape='record', style='filled', fontname='Arial')

# Definição dos objetos principais
refined_object_diagram.node('usuario', '''{usuario: Usuario|
consulta = "smartphone"\\l
}''', color='#87CEEB')  # Azul Claro

refined_object_diagram.node('interface', '''{interface: InterfaceUsuario|
resultados = [Produto1, Produto2]\\l
}''', color='#FFD700')  # Amarelo

refined_object_diagram.node('coletor', '''{coletor: ColetorDeDados|
plataformas = [Amazon, MercadoLivre]\\l
}''', color='#D8BFD8')  # Roxo

refined_object_diagram.node('produto1', '''{produto1: Produto|
nome = "Smartphone X"\\l
preco = 1500.0\\l
loja = "Amazon"\\l
}''', color='#87CEEB')  # Azul Claro

refined_object_diagram.node('produto2', '''{produto2: Produto|
nome = "Smartphone Y"\\l
preco = 1400.0\\l
loja = "MercadoLivre"\\l
}''', color='#87CEEB')  # Azul Claro

# Relacionamentos entre os objetos, com melhor organização
refined_object_diagram.edge('usuario', 'interface', label='envia consulta')
refined_object_diagram.edge('interface', 'coletor', label='aciona coleta')
refined_object_diagram.edge('coletor', 'produto1', label='retorna dados')
refined_object_diagram.edge('coletor', 'produto2', label='retorna dados')
refined_object_diagram.edge('interface', 'produto1', label='exibe produto')
refined_object_diagram.edge('interface', 'produto2', label='exibe produto')

# Renderizando o diagrama refinado
refined_object_diagram_filepath = '/mnt/data/diagrama_objeto_comparador_precos_refinado'
refined_object_diagram.render(refined_object_diagram_filepath, view=False)
refined_object_diagram_filepath + '.png'
