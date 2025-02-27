from graphviz import Digraph

# Criação do diagrama de visão geral da interação
interaction_overview_diagram = Digraph('Diagrama de Visão Geral da Interação', format='png')
interaction_overview_diagram.attr(rankdir='TB', fontsize='10')

# Elementos do diagrama
interaction_overview_diagram.node('Inicio', 'Início', shape='circle', style='filled', fillcolor='black', fontcolor='white')
interaction_overview_diagram.node('EnvioConsulta', 'Usuário envia consulta', shape='rect', style='filled', fillcolor='#ffcc99')
interaction_overview_diagram.node('ColetaDados', 'Interface aciona coleta de dados', shape='rect', style='filled', fillcolor='#ffff99')
interaction_overview_diagram.node('BuscaProduto', 'Coletor busca dados do produto', shape='rect', style='filled', fillcolor='#99ccff')
interaction_overview_diagram.node('ExibeProduto', 'Interface exibe produtos', shape='rect', style='filled', fillcolor='#99ff99')
interaction_overview_diagram.node('Fim', 'Fim', shape='doublecircle', style='filled', fillcolor='black', fontcolor='white')

# Fluxo da interação
interaction_overview_diagram.edge('Inicio', 'EnvioConsulta')
interaction_overview_diagram.edge('EnvioConsulta', 'ColetaDados')
interaction_overview_diagram.edge('ColetaDados', 'BuscaProduto')
interaction_overview_diagram.edge('BuscaProduto', 'ExibeProduto')
interaction_overview_diagram.edge('ExibeProduto', 'Fim')

# Geração do diagrama
interaction_overview_diagram.render('diagrams/generated/diagrama_visao_geral_interacao')
