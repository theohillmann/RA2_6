# Analisador Sintático

Este projeto implementa um analisador sintático completo, incluindo construção de gramática, cálculo de conjuntos FIRST e FOLLOW, análise de tokens e geração de árvore sintática.

## Estrutura do Projeto

```
.
├── main.py                 # Ponto de entrada do programa
├── build_grammar/         # Módulo de construção da gramática
│   ├── build_grammar.py   # Construção da gramática
│   ├── calcular_first.py  # Cálculo do conjunto FIRST
│   ├── calcular_follow.py # Cálculo do conjunto FOLLOW
│   ├── constants.py       # Constantes do projeto
│   └── utils.py          # Funções utilitárias
├── gerar_arvore/         # Módulo de geração da árvore sintática
│   └── gerar_arvore.py   # Geração e visualização da árvore
├── ler_tokens/           # Módulo de leitura de tokens
│   └── ler_tokens.py     # Processamento de arquivos de tokens
├── parsear/             # Módulo de análise sintática
│   └── parsear.py       # Implementação do parser
└── tokens/              # Arquivos de teste
    ├── test1.json      # Arquivo de tokens de teste 1
    ├── test1.txt       # Resultado esperado do teste 1
    ├── test2.json      # Arquivo de tokens de teste 2
    ├── test2.txt       # Resultado esperado do teste 2
    ├── test3.json      # Arquivo de tokens de teste 3
    └── test3.txt       # Resultado esperado do teste 3
```

## Funcionalidades

- Construção automática de gramática
- Cálculo de conjuntos FIRST e FOLLOW
- Análise de tokens de entrada
- Geração de árvore sintática
- Visualização da árvore de análise
- Suporte a múltiplos arquivos de teste

## Como Usar

1. Certifique-se de ter Python instalado em seu sistema

2. Clone o repositório:
```bash
git clone https://github.com/theohillmann/RA2_6.git
cd RA2_6
```

3. Execute o programa com um arquivo de tokens:
```bash
python main.py tokens/test1.txt
```

## Formato dos Arquivos de Entrada

Os arquivos de tokens devem estar no formato txt e seguir a estrutura esperada pelo analisador. Exemplos podem ser encontrados no diretório `tokens/`.

## Estrutura de Módulos

### build_grammar/
- **build_grammar.py**: Responsável pela construção da gramática
- **calcular_first.py**: Implementa o algoritmo de cálculo do conjunto FIRST
- **calcular_follow.py**: Implementa o algoritmo de cálculo do conjunto FOLLOW
- **constants.py**: Define constantes utilizadas no projeto
- **utils.py**: Funções auxiliares para manipulação da gramática

### gerar_arvore/
- **gerar_arvore.py**: Implementa a geração e visualização da árvore sintática

### ler_tokens/
- **ler_tokens.py**: Processa e valida os arquivos de tokens de entrada

### parsear/
- **parsear.py**: Implementa o analisador sintático

## Testes

O diretório `tokens/` contém arquivos de teste para validar o funcionamento do analisador:
- `test1.txt`, `test2.txt`, `test3.txt`: Arquivos com as expressões a serem analisadas

## Autores

Theo Hillmann Luiz Coelho

Projeto desenvolvido para a disciplina de Compiladores - PUCPR


