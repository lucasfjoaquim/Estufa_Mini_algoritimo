<a name="API"></a>

<br />
<div align="center">
  <a href="#">
    <img src="images/logo.png" alt="Logo" width="auto" height="80">
  </a>
</div>

## Sobre o projeto

<div>
<p>Este Algoritmo Assincrono foi desenvolvido para tirar a carga de
processamentos de dados da <a>API</a> deixando assim seu response time mais rapido <br><br>
Deve ser usado em conjunto com a <a href="https://github.com/FIAP-grupo-challenge/Python_GS">API</a></p>
<p>Areas que o Algoritmo Assincrono afeta: <br>
* Banco de dados <br>
</p>
</div>
<div align="center">

</div>

## Dependencias

1. <a href="https://pypi.org/project/python-dotenv/">Python-dotenv</a> : python-dotenv é uma biblioteca em Python que permite carregar variáveis de ambiente de um arquivo .env para facilitar a configuração de uma aplicação.
2. <a href="https://pypi.org/project/psycopg2/">Psycopg2-binary</a> : psycopg2 é uma biblioteca em Python que fornece uma interface para se conectar e interagir com bancos de dados PostgreSQL. Estamos utilzando a versão "binary" Para evitar problemas de compatibilidade com a biblioteca <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask</a>

## Instalação

1. Clonar o respositorio
    ```sh
    git clone https://github.com/FIAP-grupo-challenge/Python_algoritimo_assincrono_GS
    ```
2. Instalar dependencias
    ```sh
    pip install -r requirements.txt
    ```
3. rodar arquivo run.py


## Funcionalidades
Este Algoritimo preve a atualização dos campos status e warnings de cada planta individual no banco de dados, devido a 
grande carga de dados e uma necessidade de executar esse codigo em curtos intervalos de tempo para que haja uma
boa experiencia do cliente.
Decidimos optar pelo modelo Assincrono, isto é, opera de modo independente das outras funcionladiades, 
sem precisar de chamadas ou imputs (com exeção do banco de dados)

## Funcionamento
puxamos os dados da planta do banco de dados, verificamos seu ultimo 
registro com informações do ambiente, e fazemos diversas comparações 
dinamicas para determinar a saude da planta de acordo com as leituras 
dos scensores arduino, e com o seu tipo
(Tomate, Pimentão, Abobrinha, Alface, Rúcula, Espinafre, Feijão, Ervilha,
Lentilha, Cenoura, Beterraba, Rabanete) São os inclusos atualmente neste algoritimo.
<br>
<a href="https://docs.google.com/document/d/1Cksx6UsUF8wGBm-A323HxZ9ASwI1IkP1oj8LSV79PgM">Documentação referencia</a>,
 <a href="https://docs.google.com/spreadsheets/d/1H01g-dSNPxh0MEEofo5OklKyFkWevS91xhuCoi0P0Is">Formulas das comparações</a>.

## Banco de dados

<div>
<p>
Para uma documentação mais completa do Banco visite o respositorio <a href="https://github.com/FIAP-grupo-challenge/Banco_de_dados_GS">Banco de Dados</a></A><br><br>
O banco de dados escolhido para esta aplicação foi <a href="https://www.postgresql.org">PostgreSQL</a><br><br>
Motivos desta escolha: <br><br>
* Maturidade e estabilidade: O PostgreSQL tem uma história de desenvolvimento longa e bem estabelecida, remontando a mais de 30 anos. Ele é conhecido por sua confiabilidade, robustez e estabilidade, sendo amplamente utilizado em ambientes de produção exigentes.<br>
* Suporte a SQL completo: O PostgreSQL adere estritamente aos padrões ANSI SQL e oferece suporte a um amplo conjunto de recursos SQL, incluindo subconsultas, junções complexas, desencadeadores (triggers), procedimentos armazenados e muito mais. Isso torna o PostgreSQL altamente compatível com outras bases de dados e facilita a migração de aplicativos de outros sistemas de gerenciamento de banco de dados.<br>
* Extensibilidade: O PostgreSQL é altamente extensível, permitindo que os usuários adicionem novos tipos de dados, funções, operadores e até mesmo recursos personalizados por meio de extensões. Além disso, ele suporta várias linguagens de programação (como PL/pgSQL, PL/Python, PL/Java) para escrever procedimentos armazenados e funções personalizadas.<br>
* Recursos avançados: O PostgreSQL possui uma ampla gama de recursos avançados, incluindo suporte a transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade), replicação síncrona e assíncrona, particionamento de tabelas, índices avançados (como índices GIN e GiST para pesquisa de texto completo e dados geométricos), entre outros. Esses recursos fornecem flexibilidade e desempenho aprimorado para uma variedade de casos de uso.<br>
* Suporte a dados geoespaciais: O PostgreSQL possui suporte nativo a dados geoespaciais, permitindo a realização de consultas e operações complexas em dados com componentes espaciais. Isso é particularmente útil para aplicativos de mapeamento, sistemas de informação geográfica (GIS) e análises baseadas em localização.<br>
* Comunidade ativa: O PostgreSQL possui uma comunidade de usuários ativa e engajada, que contribui com melhorias, correções de bugs e desenvolvimento contínuo do sistema. Essa comunidade vibrante resulta em um software de alta qualidade, suporte técnico abrangente e ampla disponibilidade de recursos e tutoriais online.<br>
* Licença de código aberto: O PostgreSQL é distribuído sob a licença PostgreSQL, que é uma licença de código aberto. Isso significa que você pode usá-lo, modificá-lo e distribuí-lo gratuitamente, além de ter acesso ao código-fonte completo. A licença de código aberto promove a transparência, flexibilidade e independência em relação a um fornecedor específico.
</p><br>
<p>Conexão da API com o Banco: <br><br>
A conexão é feita por meio da biblioteca do Python <a href="https://pypi.org/project/psycopg2/">psycopg2</a> utilizando a URL de conexão como parametro</p><br>
<p>Credenciais de conexão:<br><br>
A credencial de conexão via URL se encontra no arquivo .env</p><br>
<p>Hospedagem do banco de dados:<br><br>
O banco de dados atualmente se econtra hospedado com o serviço gratuito <a href="https://www.elephantsql.com">ElephantSQL</a></p></div>

## Desenvolvedores
1. Nome: Lucas Fernandes Joaquim, RM: 551313
2. Nome: Gustavo Ferreira Lopes, RM: 98887
3. Nome: heitor freire dos anjos, RM: 552165
4. Nome: Rodrigo Fernandes dos Santos, RM: 98896
5. Nome: Enzo Silva Cataldi, RM: 99826