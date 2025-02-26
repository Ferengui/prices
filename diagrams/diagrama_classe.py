# Criação do Diagrama de Classe UML
class_diagram = Digraph(comment='Diagrama de Classe - Comparador de Preços', format='png')
class_diagram.attr(rankdir='TB', fontsize='10')
class_diagram.attr('node', shape='record', style='filled', color='#f7f7f7', fontname='Arial')

# Definição das classes principais
class_diagram.node('Produto', '''{Produto|
- id: int\\l
- nome: string\\l
- preco: float\\l
- url: string\\l
- loja: string\\l|
+ getDetalhes(): string\\l
}''', color='#87CEEB')

class_diagram.node('Plataforma', '''{Plataforma|
- nome: string\\l
- url_api: string\\l|
+ buscarProdutos(consulta: string): List<Produto>\\l
}''', color='#D8BFD8')

class_diagram.node('ColetorDeDados', '''{ColetorDeDados|
- plataformas: List<Plataforma>\\l|
+ coletar(consulta: string): List<Produto>\\l
}''', color='#D8BFD8')

class_diagram.node('MotorDeComparacao', '''{MotorDeComparacao|
- produtos: List<Produto>\\l|
+ ordenarPorPreco(): List<Produto>\\l
}''', color='#D8BFD8')

class_diagram.node('InterfaceUsuario', '''{InterfaceUsuario|
+ exibirResultados(produtos: List<Produto>)\\l
+ receberConsulta(): string\\l
}''', color='#FFD700')

# Relacionamentos entre as classes
class_diagram.edge('ColetorDeDados', 'Plataforma', label='usa')
class_diagram.edge('ColetorDeDados', 'Produto', label='retorna')
class_diagram.edge('MotorDeComparacao', 'Produto', label='ordena')
class_diagram.edge('InterfaceUsuario', 'MotorDeComparacao', label='consulta')
class_diagram.edge('InterfaceUsuario', 'ColetorDeDados', label='aciona')
class_diagram.edge('MotorDeComparacao', 'Produto', label='exibe')

# Renderização do diagrama
class_diagram_filepath = '/mnt/data/diagrama_classe_comparador_precos'
class_diagram.render(class_diagram_filepath, view=False)
class_diagram_filepath + '.png'
