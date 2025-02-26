# Criação do Diagrama de Pacote UML
package_diagram = Digraph(comment='Diagrama de Pacote - Comparador de Preços', format='png')
package_diagram.attr(rankdir='TB', fontsize='10')
package_diagram.attr('node', shape='folder', style='filled', color='#f7f7f7', fontname='Arial')

# Definição dos pacotes principais
package_diagram.node('Interface', 'Pacote: Interface', color='#FFD700')
package_diagram.node('Servicos', 'Pacote: Serviços', color='#D8BFD8')
package_diagram.node('Modelos', 'Pacote: Modelos', color='#87CEEB')
package_diagram.node('Conectores', 'Pacote: Conectores', color='#90EE90')
package_diagram.node('Utilitarios', 'Pacote: Utilitários', color='#D8BFD8')

# Definindo as dependências entre os pacotes
package_diagram.edge('Interface', 'Servicos', label='usa')
package_diagram.edge('Servicos', 'Modelos', label='manipula')
package_diagram.edge('Servicos', 'Conectores', label='consome')
package_diagram.edge('Conectores', 'Modelos', label='retorna dados')
package_diagram.edge('Servicos', 'Utilitarios', label='utiliza')
package_diagram.edge('Interface', 'Modelos', label='exibe')

# Renderização do diagrama
package_diagram_filepath = '/mnt/data/diagrama_pacote_comparador_precos'
package_diagram.render(package_diagram_filepath, view=False)
package_diagram_filepath + '.png'
