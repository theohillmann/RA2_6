# Analisador Sintático RPN - Fase 2

## Informações Institucionais
- **Instituição**: Pontifícia Universidade Católica do Paraná (PUCPR)
- **Disciplina**: Compiladores
- **Professor**: [Nome do Professor]
- **Ano/Semestre**: 2024
- **Grupo**: RA2_6

## Integrantes
- Theo Hillmann Luiz Coelho - [@theohillmann](https://github.com/theohillmann)

## Descrição do Projeto

Este projeto implementa um **Analisador Sintático LL(1)** para uma linguagem de programação simplificada que utiliza **Notação Polonesa Reversa (RPN)**. O analisador processa tokens de entrada e gera uma árvore sintática representando a estrutura hierárquica do código.

### Fase 2 - Características Implementadas

- ✅ Parser LL(1) descendente recursivo com pilha
- ✅ Cálculo automático de conjuntos FIRST e FOLLOW
- ✅ Construção de tabela de análise LL(1) sem conflitos
- ✅ Geração de árvore sintática com visualização ASCII
- ✅ Suporte a operações aritméticas: `+`, `-`, `*`, `|`, `/`, `%`, `^`
- ✅ Suporte a operadores relacionais: `>`, `<`, `>=`, `<=`, `==`, `!=`
- ✅ Comandos especiais: `RES` (resultado anterior), `MEM` (memória)
- ⚠️ Estruturas de controle: `if`, `while` (parcialmente funcional)
- ✅ Tratamento de erros sintáticos com mensagens descritivas
- ✅ Serialização de árvores sintáticas em JSON

## Instalação e Requisitos

### Requisitos
- Python 3.8 ou superior
- Nenhuma dependência externa (usa apenas biblioteca padrão)

### Estrutura do Projeto
```
RA2_6/
├── main.py                      # Ponto de entrada principal
├── build_grammar/               # Módulo de construção da gramática
│   ├── build_grammar.py         # Constrói gramática e tabela LL(1)
│   ├── calcular_first.py        # Calcula conjuntos FIRST
│   ├── calcular_follow.py       # Calcula conjuntos FOLLOW
│   ├── constants.py             # Definições da gramática
│   └── utils.py                 # Funções auxiliares
├── parsear/                     # Módulo do parser
│   └── parsear.py              # Implementação do parser LL(1)
├── ler_tokens/                  # Módulo de leitura de tokens
│   └── ler_tokens.py           # Lê e normaliza tokens
├── gerar_arvore/                # Módulo de geração de árvore
│   └── gerar_arvore.py         # Gera e visualiza árvore sintática
├── tokens/                      # Arquivos de teste
│   ├── test1.txt               # Arquivo de teste 1
│   ├── tokens.txt              # Arquivo de teste principal
│   └── invalid.txt             # Testes de erros
├── RELATORIO_AVALIACAO.md      # Relatório de avaliação completo
├── DOCUMENTACAO_GRAMATICA.md   # Documentação técnica da gramática
└── README.md                   # Este arquivo
```

## Como Usar

### Execução Básica

```bash
# Executar com arquivo de teste padrão (hardcoded)
python3 main.py

# Para usar arquivo customizado, modifique a linha 65 de main.py:
# f = "tokens/seu_arquivo.txt"
```

### Formato dos Arquivos de Entrada

Os arquivos de entrada devem conter uma expressão por linha em notação RPN:

```
( 10 8 + )
( 35 13 - )
( 5 6 * )
( 27 9 / )
( ( A B + ) ( C D * ) | )
( 5 res )
( 42 v TOTAL )
( ( A B > ) ( X ) ( Y ) if )
```

### Exemplos de Sintaxe

#### Operações Aritméticas
```
( 10 8 + )              # Adição: 10 + 8
( 35 13 - )             # Subtração: 35 - 13
( 5 6 * )               # Multiplicação: 5 * 6
( 27 9 / )              # Divisão inteira: 27 / 9
( 27 9 | )              # Divisão real: 27.0 / 9.0
( 17 6 % )              # Resto: 17 % 6
( 4 3 ^ )               # Potência: 4^3
```

#### Expressões Aninhadas
```
( ( A B + ) ( C D - ) * )       # (A + B) * (C - D)
( ( X 2 * ) ( Y 3 * ) + )       # (X * 2) + (Y * 3)
```

#### Comandos Especiais
```
( 5 res )               # Retorna resultado 5 linhas atrás
( 42 v TOTAL )          # Armazena 42 na memória TOTAL
( TOTAL )               # Recupera valor de TOTAL
```

#### Operadores Relacionais
```
( A B > )               # A > B
( X Y < )               # X < Y
( I J >= )              # I >= J
( P Q == )              # P == Q
```

#### Estruturas de Controle (Sintaxe Experimental)
```
( ( A B > ) ( X ) ( Y ) if )                    # if A > B then X else Y
( ( I N < ) ( ( I 1 + ) v I ) while )           # while I < N do I = I + 1
```

**Nota**: As estruturas de controle têm limitações conhecidas (veja seção de Limitações).

## Saída do Programa

O programa gera:

1. **Saída no console**:
   - Status de cada expressão (aceita/erro)
   - Árvore sintática em formato ASCII
   - Resumo de expressões processadas

2. **Arquivo JSON**:
   - Árvores sintáticas serializadas
   - Nome: `<arquivo_entrada>.json`
   - Exemplo: `tokens/test1.json`

### Exemplo de Saída
```
=== Expressão 1 ===
Tokens: ( int int + ) $
✅ Expressão aceita. Derivação com 13 produções.

Árvore sintática (ASCII):
└─ PROGRAM
   └─ LINES
      ├─ LINE
      │  └─ SEXP
      │     ├─ (
      │     ├─ FORM
      │     │  ├─ STACKTERM
      │     │  │  └─ VALUE
      │     │  │     └─ int
      │     │  └─ TAIL1
      │     │     ├─ STACKTERM
      │     │     │  └─ VALUE
      │     │     │     └─ int
      │     │     └─ TAIL2
      │     │        └─ OP
      │     │           └─ +
      │     └─ )
      └─ LINES

Resumo: 1 aceitas, 0 com erro.
Árvores salvas em: tokens/test1.json
```

## Gramática Implementada

A gramática completa está documentada em [DOCUMENTACAO_GRAMATICA.md](DOCUMENTACAO_GRAMATICA.md).

### Resumo da Gramática (EBNF)
```
PROGRAM      = LINES ;
LINES        = LINE LINES | ε ;
LINE         = SEXP ;
SEXP         = "(" FORM ")" ;
FORM         = STACKTERM TAIL1 ;
TAIL1        = STACKTERM TAIL2 | "res" | "v" "memid" | ε ;
TAIL2        = OP | STACKTERM "if" | "while" ;
STACKTERM    = VALUE | SEXP ;
VALUE        = "int" | "real" | "memid" ;
OP           = "+" | "-" | "*" | "|" | "/" | "%" | "^" 
             | ">" | "<" | ">=" | "<=" | "==" | "!=" ;
```

### Propriedades
- **Gramática LL(1)**: Sim (sem conflitos)
- **Não-terminais**: 10
- **Terminais**: 23
- **Produções**: 31
- **Entradas na tabela LL(1)**: 55

## Testes

### Arquivos de Teste Incluídos
- `tokens/test1.txt` - 2 expressões simples
- `tokens/tokens.txt` - 51 expressões variadas (principal)
- `tokens/invalid.txt` - 6 casos de erro

### Executar Testes
```bash
# Teste principal
python3 main.py

# Verificar testes manualmente
python3 -c "from main import main; main('tokens/tokens.txt')"
```

### Cobertura dos Testes
- ✅ Todas as operações aritméticas: +, -, *, |, /, %, ^
- ✅ Todos os operadores relacionais: >, <, >=, <=, ==, !=
- ✅ Comandos especiais: res, v
- ✅ Expressões aninhadas
- ⚠️ Estruturas de controle (parcialmente)

## Limitações Conhecidas

1. **Estruturas de Controle Complexas**
   - A gramática atual não aceita corpos de IF/WHILE que contenham operações de store (v) seguidas de operadores
   - 9 de 51 expressões de teste falharam
   - Exemplo que falha: `( ( I N < ) ( ( I 1 + ) ( v I ) ) while )`

2. **Argumentos de Linha de Comando**
   - O programa atualmente usa arquivo hardcoded (linha 65 de main.py)
   - Para alterar, edite manualmente o código

3. **Recuperação de Erros**
   - O parser para no primeiro erro sintático sem tentativa de recuperação

## Documentação Adicional

- **[RELATORIO_AVALIACAO.md](RELATORIO_AVALIACAO.md)**: Relatório completo de avaliação do projeto com pontuação detalhada
- **[DOCUMENTACAO_GRAMATICA.md](DOCUMENTACAO_GRAMATICA.md)**: Documentação técnica incluindo:
  - Gramática completa em EBNF
  - Conjuntos FIRST e FOLLOW
  - Tabela de análise LL(1)
  - Exemplos de árvores sintáticas
  - Análise de complexidade

## Contribuindo

Este é um projeto acadêmico. Contribuições devem ser feitas via pull requests no GitHub.

### Workflow de Desenvolvimento
1. Fork do repositório
2. Criar branch para feature (`git checkout -b feature/MinhaFeature`)
3. Commit das mudanças (`git commit -m 'Add: MinhaFeature'`)
4. Push para o branch (`git push origin feature/MinhaFeature`)
5. Abrir Pull Request

## Licença

Este é um projeto acadêmico desenvolvido para fins educacionais na disciplina de Compiladores.

## Contato

- Theo Hillmann Luiz Coelho - [@theohillmann](https://github.com/theohillmann)
- Repositório: [https://github.com/theohillmann/RA2_6](https://github.com/theohillmann/RA2_6)

---

*Projeto desenvolvido como parte da disciplina de Compiladores - Fase 2: Análise Sintática*