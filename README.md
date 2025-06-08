🗺️ Sistema de Grafo de Cidades
Este projeto é um sistema de linha de comando (CLI) simples, desenvolvido em Python, para criar, gerenciar e visualizar um grafo de cidades e suas conexões. A aplicação permite registrar cidades (vértices) e as distâncias entre elas (arestas ponderadas), persistindo todos os dados em arquivos CSV.

✨ Funcionalidades Principais
Cadastro de Cidades: Adiciona novas cidades (vértices) ao grafo.
Cadastro de Conexões: Cria conexões (arestas) entre duas cidades com uma distância específica (peso).
Listagem de Dados: Exibe todas as cidades e conexões registradas.
Consulta de Vizinhos: Permite consultar e listar todas as cidades diretamente conectadas a uma cidade específica.
Persistência de Dados: Todas as informações são salvas em arquivos cidades.csv e conexoes.csv, garantindo que os dados não sejam perdidos ao fechar o programa.
Interface de Linha de Comando: Menu interativo para facilitar o uso de todas as funcionalidades.
🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal do projeto.
Módulos Nativos: Utiliza apenas as bibliotecas padrão do Python, sem necessidade de instalar dependências externas.
csv: Para manipulação dos arquivos de dados.
os: Para verificação da existência de arquivos.
📂 Estrutura do Projeto
O projeto está organizado da seguinte forma:

/seu-projeto-grafos
|
|-- main.py             # Arquivo principal, contém o menu e a interface do usuário.
|-- classes.py          # Contém as definições das classes (Grafo, City, Edge).
|-- cidades.csv         # Armazena os nomes das cidades cadastradas.
|-- conexoes.csv        # Armazena as conexões entre as cidades e suas distâncias.
|-- README.md           # Este arquivo.
🚀 Como Executar
Para rodar o projeto em sua máquina local, siga os passos abaixo.

Pré-requisitos
Ter o Python 3 instalado em seu sistema.
Passos
Clone o repositório (ou baixe os arquivos):
Se o projeto estiver no GitHub, use o comando abaixo. Caso contrário, apenas certifique-se de que os arquivos main.py e classes.py estejam na mesma pasta.

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Navegue até a pasta do projeto:
Abra um terminal ou prompt de comando na pasta onde os arquivos do projeto estão localizados.

Execute o programa:
Digite o seguinte comando no terminal:

Bash

python main.py
Interaja com o menu:
O menu principal será exibido no terminal. Escolha as opções de 1 a 6 para interagir com o sistema. Os arquivos cidades.csv e conexoes.csv serão criados automaticamente na primeira execução, caso não existam.

⚙️ Como Funciona
O sistema é dividido em duas partes principais:

classes.py: Contém a lógica de negócios e a estrutura de dados.

A classe Grafo gerencia todas as operações, como adicionar vértices/arestas e carregar/salvar os dados nos arquivos CSV.
As classes City e Edge modelam os vértices e as arestas do grafo.
main.py: É responsável pela camada de apresentação e interação com o usuário.

Ele importa o Grafo do arquivo de classes, carrega os dados existentes dos arquivos CSV e exibe um menu de opções em um loop contínuo.
Cada opção do menu chama um método correspondente no objeto Grafo para executar a ação desejada.
👤 Autor
[Seu Nome Aqui]

GitHub: @AlexandreD-Martins
LinkedIn: https://www.linkedin.com/in/alexandre-dmartins/
