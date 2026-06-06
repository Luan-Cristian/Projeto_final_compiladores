# Gerenciador de Tabela de Símbolos com Escopos Aninhados

## 1. Descrição do projeto

Este projeto implementa um **Gerenciador de Tabela de Símbolos**, tema relacionado à fase de **análise semântica** de compiladores.

A tabela de símbolos é responsável por armazenar informações sobre identificadores declarados em um programa, como nome da variável, tipo e escopo onde foi declarada.

O sistema utiliza:

- Uma **pilha de escopos**;
- **Hash Tables**, implementadas com dicionários Python;
- Métodos para declarar variáveis;
- Métodos para buscar variáveis em escopos aninhados;
- Verificação de erro para variável não declarada;
- Verificação de erro para redeclaração no mesmo escopo.

## 2. Estrutura do pacote

```text
gerenciador-tabela-simbolos/
│
├── main.py
├── tabela_simbolos.py
├── README.md
├── relatorio.pdf
└── exemplos/
    ├── teste_escopo.txt
    ├── teste_erro_redeclaracao.txt
    └── teste_busca_variavel.txt
```

## 3. Requisitos

Para executar o projeto, é necessário ter o Python instalado.

Versão recomendada:

```bash
Python 3.10 ou superior
```

Não é necessário instalar bibliotecas externas.

## 4. Como executar

No terminal, entre na pasta do projeto:

```bash
cd gerenciador-tabela-simbolos
```

Execute o programa principal:

```bash
python main.py
```

Em alguns sistemas, o comando pode ser:

```bash
python3 main.py
```

## 5. Modos de execução

Ao iniciar o programa, serão exibidas duas opções:

```text
1 - Executar testes automaticos
2 - Usar menu interativo
```

### Modo 1 - Testes automáticos

Executa uma sequência pronta demonstrando:

- Declaração de variáveis;
- Criação de escopos aninhados;
- Busca de variáveis;
- Sombreamento de variável;
- Erro de redeclaração;
- Erro de variável não declarada;
- Remoção de escopo.

### Modo 2 - Menu interativo

Permite testar manualmente as operações:

```text
1 - Declarar variavel
2 - Buscar variavel
3 - Entrar em novo escopo
4 - Sair do escopo atual
5 - Mostrar tabela
0 - Encerrar
```

## 6. Exemplo de saída

```text
[OK] Variavel 'x' declarada como 'int' no escopo 0.
[OK] Novo escopo criado. Nivel atual: 1
[OK] Variavel 'x' declarada como 'float' no escopo 1.
[OK] Variavel 'x' encontrada no escopo 1. Tipo: float
[OK] Escopo de nivel 1 removido. Nivel atual: 0
[OK] Variavel 'x' encontrada no escopo 0. Tipo: int
```

## 7. Relação com Compiladores

Durante a análise semântica, o compilador precisa verificar se as variáveis utilizadas foram declaradas, se estão visíveis no escopo atual e qual tipo foi associado a cada identificador.

Este projeto simula exatamente esse comportamento usando uma pilha de tabelas hash, onde cada escopo possui suas próprias declarações.
