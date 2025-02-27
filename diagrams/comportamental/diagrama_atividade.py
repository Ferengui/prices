# Criando o Diagrama de Atividade UML para o Comparador de Preços
activity_diagram = Digraph(comment='Diagrama de Atividade - Comparador de Preços', format='png')
activity_diagram.attr(rankdir='TB', fontsize='10')
activity_diagram.attr('node', shape='box', style='filled', fontname='Arial', color='#D8BFD8')

# Início do processo
activity_diagram.node('inicio', 'Início', shape='circle', style='filled', color='black', fontcolor='white')

# Atividades principais
activity_diagram.node('receberConsulta', 'Receber Consulta do Usuário', color='#FFD700')  # Interface Usuário
activity_diagram.node('validarConsulta', 'Validar Consulta', color='#D8BFD8')  # Backend
activity_diagram.node('coletarDados', 'Acionar Coleta de Dados', color='#D8BFD8')  # Coletor
activity_diagram.node('consultarAPIs', 'Consultar APIs Externas', color='#87CEEB')  # Plataformas Externas
activity_diagram.node('armazenarDados', 'Armazenar Dados no Banco', color='#87CEEB')  # Banco de Dados
activity_diagram.node('processarDados', 'Processar e Ordenar Dados', color='#D8BFD8')  # Backend
activity_diagram.node('exibirResultados', 'Exibir Resultados ao Usuário', color='#FFD700')  # Interface Usuário

# Fim do processo
activity_diagram.node('fim', 'Fim', shape='doublecircle', style='filled', color='black', fontcolor='white')

# Fluxo do processo
activity_diagram.edge('inicio', 'receberConsulta')
activity_diagram.edge('receberConsulta', 'validarConsulta')
activity_diagram.edge('validarConsulta', 'coletarDados')
activity_diagram.edge('coletarDados', 'consultarAPIs')
activity_diagram.edge('consultarAPIs', 'armazenarDados')
activity_diagram.edge('armazenarDados', 'processarDados')
activity_diagram.edge('processarDados', 'exibirResultados')
activity_diagram.edge('exibirResultados', 'fim')

# Renderizando o diagrama de atividade
activity_diagram_filepath = 'activity_diagram.render('diagrams/generated/diagrama_atividade')'
activity_diagram.render(activity_diagram_filepath, view=False)
activity_diagram_filepath + '.png'
