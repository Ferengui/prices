from graphviz import Digraph

# Criação do diagrama de transição de estados
state_diagram = Digraph('Diagrama de Transição de Estados', format='png')
state_diagram.attr(rankdir='LR', fontsize='10')

# Estados
state_diagram.node('Inicio', '', shape='circle', style='filled', fillcolor='black')
state_diagram.node('ConsultaEnviada', 'Consulta Enviada', shape='box', style='filled', fillcolor='#ffcc99')
state_diagram.node('ColetaDados', 'Coleta de Dados', shape='box', style='filled', fillcolor='#99ccff')
state_diagram.node('ExibicaoProdutos', 'Exibição de Produtos', shape='box', style='filled', fillcolor='#99ff99')
state_diagram.node('Fim', '', shape='doublecircle', style='filled', fillcolor='black')

# Transições
state_diagram.edge('Inicio', 'ConsultaEnviada', label='envia consulta')
state_diagram.edge('ConsultaEnviada', 'ColetaDados', label='aciona coleta')
state_diagram.edge('ColetaDados', 'ExibicaoProdutos', label='dados coletados')
state_diagram.edge('ExibicaoProdutos', 'Fim', label='exibe produtos')

# Geração do diagrama
state_diagram.render('diagrams/generated/diagrama_transicao_estados')
