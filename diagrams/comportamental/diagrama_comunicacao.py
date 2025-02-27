from graphviz import Digraph

# Criação do diagrama de comunicação
communication_diagram = Digraph('Diagrama de Comunicação', format='png')
communication_diagram.attr(rankdir='LR', fontsize='10')

# Elementos do diagrama
communication_diagram.node('Usuario', 'Usuário', shape='rect', style='filled', fillcolor='#ffcc99')
communication_diagram.node('Interface', 'Interface de Usuário', shape='rect', style='filled', fillcolor='#ffff99')
communication_diagram.node('Coletor', 'Coletor de Dados', shape='rect', style='filled', fillcolor='#99ccff')
communication_diagram.node('Produto', 'Produto', shape='rect', style='filled', fillcolor='#99ff99')

# Mensagens entre os objetos
communication_diagram.edge('Usuario', 'Interface', label='1. envia consulta')
communication_diagram.edge('Interface', 'Coletor', label='2. aciona coleta')
communication_diagram.edge('Coletor', 'Produto', label='3. busca dados do produto')
communication_diagram.edge('Produto', 'Coletor', label='4. retorna dados')
communication_diagram.edge('Coletor', 'Interface', label='5. envia dados para exibição')
communication_diagram.edge('Interface', 'Usuario', label='6. exibe os produtos')

# Geração do diagrama
communication_diagram.render('diagrams/generated/diagrama_comunicacao')
