# Criando o Diagrama de Estrutura Composta UML para o Comparador de Preços
structure_diagram = Digraph(comment='Diagrama de Estrutura Composta - Comparador de Preços', format='png')
structure_diagram.attr(rankdir='TB', fontsize='10')
structure_diagram.attr('node', shape='record', style='filled', fontname='Arial')

# Definição dos componentes principais e suas estruturas internas
structure_diagram.node('interfaceUsuario', '''{InterfaceUsuario|
- exibirResultados()\\l
- receberConsulta()\\l
}''', color='#FFD700')  # Amarelo

structure_diagram.node('apiBackend', '''{API Backend|
- processarConsulta()\\l
- acessarBancoDados()\\l
- acionarColetor()\\l
}''', color='#D8BFD8')  # Roxo

structure_diagram.node('coletorDados', '''{ColetorDeDados|
- conectarAPIs()\\l
- extrairDados()\\l
- normalizarDados()\\l
}''', color='#D8BFD8')  # Roxo

structure_diagram.node('bancoDados', '''{BancoDeDados|
- armazenarDados()\\l
- consultarDados()\\l
}''', color='#87CEEB')  # Azul Claro

structure_diagram.node('produto', '''{Produto|
- nome: string\\l
- preco: float\\l
- loja: string\\l
}''', color='#87CEEB')  # Azul Claro

# Relacionamentos entre os componentes internos
structure_diagram.edge('interfaceUsuario', 'apiBackend', label='envia consulta')
structure_diagram.edge('apiBackend', 'coletorDados', label='aciona coleta')
structure_diagram.edge('apiBackend', 'bancoDados', label='consulta dados')
structure_diagram.edge('coletorDados', 'bancoDados', label='armazena dados')
structure_diagram.edge('bancoDados', 'apiBackend', label='retorna dados')
structure_diagram.edge('apiBackend', 'interfaceUsuario', label='envia resultados')

# Renderizando o diagrama de estrutura composta
structure_diagram_filepath = '/mnt/data/diagrama_estrutura_composta_comparador_precos'
structure_diagram.render(structure_diagram_filepath, view=False)
structure_diagram_filepath + '.png'
