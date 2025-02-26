# Criação do Diagrama de Objeto UML
object_diagram = Digraph(comment='Diagrama de Objeto - Comparador de Preços', format='png')
object_diagram.attr(rankdir='TB', fontsize='10')
object_diagram.attr('node', shape='record', style='filled', color='#f7f7f7', fontname='Arial')

# Definição dos objetos principais
object_diagram.node('usuario', '''{usuario: Usuario|
consulta = "smartphone"\\l
}''', color='#87CEEB')

object_diagram.node('interface', '''{interface: InterfaceUsuario|
resultados = [Produto1, Produto2, Produto3]\\l
}''', color='#FFD700')

object_diagram.node('coletor', '''{coletor: ColetorDeDados|
plataformas = [Amazon, MercadoLivre]\\l
}''', color='#D8BFD8')

object_diagram.node('produto1', '''{produto1: Produto|
nome = "Smartphone X"\\l
preco = 1500.0\\l
loja = "Amazon"\\l
}''', color='#D8BFD8')

object_diagram.node('produto2', '''{produto2: Produto|
nome = "Smartphone Y"\\l
preco = 1400.0\\l
loja = "MercadoLivre"\\l
}''', color='#D8BFD8')

# Relacionamentos entre os objetos
object_diagram.edge('usuario', 'interface', label='envia consulta')
object_diagram.edge('interface', 'coletor', label='aciona coleta')
object_diagram.edge('coletor', 'produto1', label='retorna dados')
object_diagram.edge('coletor', 'produto2', label='retorna dados')
object_diagram.edge('interface', 'produto1', label='exibe produto')
object_diagram.edge('interface', 'produto2', label='exibe produto')

# Renderização do diagrama
object_diagram_filepath = '/mnt/data/diagrama_objeto_comparador_precos'
object_diagram.render(object_diagram_filepath, view=False)
object_diagram_filepath + '.png'
