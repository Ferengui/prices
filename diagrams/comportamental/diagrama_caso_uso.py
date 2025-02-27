from graphviz import Digraph

# Criação do diagrama de caso de uso
use_case_diagram = Digraph('Diagrama de Caso de Uso', format='png')
use_case_diagram.attr(rankdir='LR', fontsize='10')

# Ator
use_case_diagram.node('Usuario', 'Usuário', shape='actor', style='filled', fillcolor='#ffcc99')

# Casos de uso
use_case_diagram.node('EnviarConsulta', 'Enviar Consulta', shape='ellipse', style='filled', fillcolor='#ffff99')
use_case_diagram.node('AcionarColeta', 'Acionar Coleta de Dados', shape='ellipse', style='filled', fillcolor='#99ccff')
use_case_diagram.node('ExibirProdutos', 'Exibir Produtos', shape='ellipse', style='filled', fillcolor='#99ff99')

# Relacionamentos
use_case_diagram.edge('Usuario', 'EnviarConsulta')
use_case_diagram.edge('EnviarConsulta', 'AcionarColeta')
use_case_diagram.edge('AcionarColeta', 'ExibirProdutos')

# Geração do diagrama
use_case_diagram.render('diagrams/generated/diagrama_caso_de_uso')
