# Criando o Diagrama de Implantação UML para o Comparador de Preços
deployment_diagram = Digraph(comment='Diagrama de Implantação - Comparador de Preços', format='png')
deployment_diagram.attr(rankdir='TB', fontsize='10')
deployment_diagram.attr('node', shape='box3d', style='filled', fontname='Arial')

# Definição dos nós físicos e servidores
deployment_diagram.node('usuario', 'Dispositivo do Usuário\n(Navegador Web)', color='#FFD700')  # Amarelo
deployment_diagram.node('servidorWeb', 'Servidor Web\n(API Backend)', color='#D8BFD8')  # Roxo
deployment_diagram.node('servidorColeta', 'Servidor Coleta de Dados\n(Coletor de Dados)', color='#D8BFD8')  # Roxo
deployment_diagram.node('servidorBD', 'Servidor de Banco de Dados\n(Banco de Dados)', color='#87CEEB')  # Azul Claro

# Definição das plataformas externas
deployment_diagram.node('apiAmazon', 'API Plataforma Amazon', shape='cylinder', color='#87CEEB')  # Azul Claro
deployment_diagram.node('apiML', 'API Mercado Livre', shape='cylinder', color='#87CEEB')  # Azul Claro

# Conexões entre os nós e componentes
deployment_diagram.edge('usuario', 'servidorWeb', label='HTTP/S (Consulta preços)')
deployment_diagram.edge('servidorWeb', 'servidorColeta', label='Requisição Coleta de Dados')
deployment_diagram.edge('servidorColeta', 'apiAmazon', label='Consulta API Amazon')
deployment_diagram.edge('servidorColeta', 'apiML', label='Consulta API Mercado Livre')
deployment_diagram.edge('servidorColeta', 'servidorBD', label='Armazena Dados')
deployment_diagram.edge('servidorBD', 'servidorWeb', label='Retorna Dados')
deployment_diagram.edge('servidorWeb', 'usuario', label='HTTP/S (Retorna resultados)')

# Renderizando o diagrama de implantação
deployment_diagram_filepath = '/mnt/data/diagrama_implantacao_comparador_precos'
deployment_diagram.render(deployment_diagram_filepath, view=False)
deployment_diagram_filepath + '.png'
