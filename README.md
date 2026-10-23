# 🌭 Fabuloso Hot Dog — LanchoneteWeb

**Sistema web para gerenciamento de pedidos de uma lanchonete, desenvolvido com Python, Flask e SQLite.**

O **LanchoneteWeb** é um projeto de desenvolvimento web que simula o funcionamento de uma lanchonete digital, permitindo que clientes consultem um cardápio, adicionem produtos ao carrinho e realizem pedidos por meio de uma interface intuitiva.

O sistema também possui uma área administrativa para gerenciamento das informações da aplicação.

---

## Sobre o projeto

O Fabuloso Hot Dog foi desenvolvido com o objetivo de colocar em prática conhecimentos de programação, desenvolvimento backend, bancos de dados relacionais e construção de interfaces web.

A aplicação utiliza **Flask** para processar requisições HTTP e implementar as regras de negócio, enquanto o **SQLite** é responsável pelo armazenamento das informações.

No frontend, HTML, CSS e templates Jinja2 são utilizados para construir páginas dinâmicas e apresentar os produtos disponíveis.

O projeto representa uma aplicação web completa de pequeno porte, integrando interface, servidor, persistência de dados e gerenciamento de sessões.

## Funcionalidades

### Cardápio digital

- Exibição dos produtos disponíveis.
- Apresentação de imagens, nomes e preços.
- Interface organizada para facilitar a navegação.
- Integração das informações dos produtos com o banco de dados.

### Carrinho de compras

- Adição de produtos ao carrinho.
- Armazenamento temporário dos itens por sessão.
- Visualização dos produtos selecionados.
- Cálculo do valor total do pedido.

### Finalização de pedidos

O sistema possui uma página de checkout na qual o cliente informa os dados necessários para realizar o pedido.

**Informações coletadas:**
- Nome do cliente.
- Telefone de contato.
- Endereço de entrega.
- Observações adicionais.

Após a confirmação, os dados do pedido são processados pela aplicação.

### Painel administrativo

- Área administrativa com autenticação.
- Controle de acesso por sessão.
- Visualização e gerenciamento das informações disponibilizadas na interface administrativa.
- Integração com o banco de dados.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal do backend |
| Flask | Framework de desenvolvimento web |
| SQLite | Banco de dados relacional |
| Jinja2 | Renderização dinâmica de templates |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Git e GitHub | Versionamento e organização do código |

## Arquitetura da aplicação

O projeto utiliza uma estrutura baseada na separação das responsabilidades da aplicação.

**Backend — Flask**

Responsável pelo processamento das requisições, gerenciamento das sessões, regras de negócio e comunicação com o banco de dados.

**Frontend — HTML, CSS e Jinja2**

Responsável pela interface de navegação, exibição do cardápio, carrinho de compras e formulários.

**Banco de dados — SQLite**

Utilizado para persistir as informações necessárias ao funcionamento do sistema, incluindo produtos e pedidos.

**Sessões**

Utilizadas para manter informações temporárias do carrinho e controlar o acesso administrativo.

## Fluxo de funcionamento

1. **Acesso ao cardápio:** o cliente visualiza os produtos cadastrados.
2. **Seleção de produtos:** os itens escolhidos são adicionados ao carrinho.
3. **Revisão do pedido:** o cliente confere os itens e o valor total.
4. **Checkout:** o cliente preenche os dados de contato e entrega.
5. **Registro do pedido:** o backend processa os dados da compra.
6. **Administração:** as informações podem ser acessadas pela área administrativa, conforme as funcionalidades implementadas.

## Executando o projeto localmente

### Pré-requisitos

Para executar a aplicação, é necessário ter instalado:

- Python 3.
- Git.
- Um editor de código, como o Visual Studio Code.

### 1. Clonar o repositório

Clone o repositório do projeto pelo GitHub ou utilize uma cópia local do código.

### 2. Criar um ambiente virtual

No terminal, dentro da pasta do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual.

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

Se o projeto possuir um arquivo `requirements.txt`, execute:

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

Verifique se a aplicação possui as tabelas necessárias para armazenar produtos e pedidos.

A inicialização e o preenchimento do banco SQLite devem seguir as rotinas implementadas no projeto.

### 5. Iniciar a aplicação

Execute o comando Flask correspondente ao módulo de entrada da aplicação.

Por exemplo, caso o arquivo principal seja `app.py`:

```bash
flask --app app run --debug
```

Depois, acesse:

`http://127.0.0.1:5000`

**Observação:** o modo de depuração deve ser utilizado apenas no ambiente de desenvolvimento.

## Conceitos aplicados

Durante o desenvolvimento do projeto, foram trabalhados diversos conceitos importantes para a construção de aplicações web:

- Organização de rotas e requisições HTTP.
- Manipulação de formulários.
- Programação backend com Python.
- Integração entre frontend e backend.
- Operações com bancos de dados relacionais.
- Gerenciamento de sessões.
- Autenticação e controle de acesso.
- Templates dinâmicos com Jinja2.
- Organização e reutilização de componentes.
- Versionamento de código com Git.

## Aprendizados e desafios

O LanchoneteWeb foi importante para consolidar meus conhecimentos em desenvolvimento web.

Um dos principais desafios foi integrar diferentes partes da aplicação, garantindo que o processo de seleção de produtos, gerenciamento do carrinho e registro dos pedidos funcionasse de maneira coordenada.

Também pude aprofundar meus conhecimentos na organização das rotas Flask, no uso de sessões e na manipulação de dados com SQLite.

O projeto contribuiu para minha evolução na construção de sistemas web que envolvem regras de negócio e persistência de informações.

## Possíveis melhorias futuras

Entre as funcionalidades que podem ser desenvolvidas futuramente estão:

- Acompanhamento do status dos pedidos.
- Integração com métodos de pagamento.
- Histórico de pedidos por cliente.
- Relatórios de vendas.
- Gerenciamento ampliado de produtos.
- Melhorias adicionais na autenticação e na segurança.
- Implantação em um ambiente de produção.

Essas funcionalidades representam possibilidades de evolução e não devem ser consideradas implementadas na versão atual.

---

## Autor

**Pedro Gavazzi**

Estudante de Ciência da Computação, com interesse em desenvolvimento de sistemas, automação e análise de dados.

**GitHub:** https://github.com/G4vazzi

**Portfólio:** https://g4vazzi.github.io/portfolio-pedro-gavazzi/

---

**Fabuloso Hot Dog — LanchoneteWeb**

*Projeto desenvolvido para fins de estudo, prática e evolução em desenvolvimento web.*
