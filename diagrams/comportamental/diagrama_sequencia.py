from graphviz import Digraph

# Criação do diagrama de sequência
sequence_diagram = Digraph('Diagrama de Sequência', format='png')
sequence_diagram.attr(rankdir='LR', fontsize='10')

# Elementos do diagrama
sequence_diagram.node('Usuario', 'Usuário', shape='rect', style='filled', fillcolor='#ffcc99')
sequence_diagram.node('Interface', 'Interface de Usuário', shape='rect', style='filled', fillcolor='#ffff99')
sequence_diagram.node('Coletor', 'Coletor de Dados', shape='rect', style='filled', fillcolor='#99ccff')
sequence_diagram.node('Produto', 'Produto', shape='rect', style='filled', fillcolor='#99ff99')

# Mensagens
sequence_diagram.edge('Usuario', 'Interface', label='envia consulta')
sequence_diagram.edge('Interface', 'Coletor', label='aciona coleta')
sequence_diagram.edge('Coletor', 'Produto', label='busca dados do produto')
sequence_diagram.edge('Produto', 'Coletor', label='retorna dados')
sequence_diagram.edge('Coletor', 'Interface', label='envia dados para exibição')
sequence_diagram.edge('Interface', 'Usuario', label='exibe os produtos')

# Geração do diagrama
sequence_diagram.render('diagrams/generated/diagrama_sequencia')
