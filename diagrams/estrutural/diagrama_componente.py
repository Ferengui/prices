# Criando o Diagrama de Componente UML para o Comparador de Preços
component_diagram = Digraph(comment='Diagrama de Componente - Comparador de Preços', format='png')
component_diagram.attr(rankdir='TB', fontsize='10')
component_diagram.attr('node', shape='component', style='filled', fontname='Arial')

# Definição dos componentes principais
component_diagram.node('interfaceUsuario', 'Interface de Usuário', color='#FFD700')  # Amarelo
component_diagram.node('apiBackend', 'API Backend', color='#D8BFD8')  # Roxo
component_diagram.node('coletorDados', 'Coletor de Dados', color='#D8BFD8')  # Roxo
component_diagram.node('plataformaAmazon', 'Plataforma Amazon', color='#87CEEB')  # Azul Claro
component_diagram.node('plataformaML', 'Plataforma Mercado Livre', color='#87CEEB')  # Azul Claro
component_diagram.node('bancoDados', 'Banco de Dados', color='#87CEEB')  # Azul Claro

# Conexões entre os componentes
component_diagram.edge('interfaceUsuario', 'apiBackend', label='Consulta Preços')
component_diagram.edge('apiBackend', 'coletorDados', label='Requisição de Coleta')
component_diagram.edge('coletorDados', 'plataformaAmazon', label='API Amazon')
component_diagram.edge('coletorDados', 'plataformaML', label='API Mercado Livre')
component_diagram.edge('coletorDados', 'bancoDados', label='Armazena Dados')
component_diagram.edge('bancoDados', 'apiBackend', label='Fornece Dados')
component_diagram.edge('apiBackend', 'interfaceUsuario', label='Retorna Resultados')

# Renderizando o diagrama de componente
component_diagram_filepath = '/mnt/data/diagrama_componente_comparador_precos'
component_diagram.render(component_diagram_filepath, view=False)
component_diagram_filepath + '.png'
