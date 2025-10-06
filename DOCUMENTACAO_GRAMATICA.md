# DOCUMENTAÇÃO TÉCNICA - GRAMÁTICA E ANÁLISE LL(1)

## 1. GRAMÁTICA EM EBNF

A gramática foi definida para reconhecer expressões em Notação Polonesa Reversa (RPN) com estruturas de controle.

```
PROGRAM      = LINES ;

LINES        = LINE LINES 
             | ε ;

LINE         = SEXP ;

SEXP         = "(" FORM ")" ;

FORM         = STACKTERM TAIL1 ;

TAIL1        = STACKTERM TAIL2 
             | "res" 
             | "v" "memid" 
             | ε ;

TAIL2        = OP 
             | STACKTERM "if" 
             | "while" ;

STACKTERM    = VALUE 
             | SEXP ;

VALUE        = "int" 
             | "real" 
             | "memid" ;

OP           = "+" | "-" | "*" | "|" | "/" | "%" | "^" 
             | ">" | "<" | ">=" | "<=" | "==" | "!=" ;
```

### Descrição dos Não-Terminais

- **PROGRAM**: Símbolo inicial, representa o programa completo
- **LINES**: Sequência de zero ou mais linhas de expressões
- **LINE**: Uma única linha contendo uma expressão
- **SEXP**: S-Expression, expressão entre parênteses
- **FORM**: Conteúdo interno de uma expressão
- **TAIL1**: Continuação após um operando (pode ser operador, comando especial ou vazio)
- **TAIL2**: Segundo operando ou estrutura de controle
- **STACKTERM**: Termo empilhável (valor ou sub-expressão)
- **VALUE**: Valor literal ou identificador de memória
- **OP**: Operador aritmético ou relacional

### Terminais

- **Literais numéricos**: `int` (inteiros), `real` (ponto flutuante)
- **Identificadores**: `memid` (nomes de variáveis/memória)
- **Operadores aritméticos**: `+`, `-`, `*`, `|` (div real), `/` (div int), `%`, `^`
- **Operadores relacionais**: `>`, `<`, `>=`, `<=`, `==`, `!=`
- **Comandos especiais**: `res` (resultado anterior), `v` (store em memória)
- **Estruturas de controle**: `if`, `while`
- **Delimitadores**: `(`, `)`
- **Fim de entrada**: `$`

## 2. CONJUNTOS FIRST

Os conjuntos FIRST indicam quais terminais podem aparecer no início de cada não-terminal.

```
FIRST(PROGRAM)     = { "(", ε }
FIRST(LINES)       = { "(", ε }
FIRST(LINE)        = { "(" }
FIRST(SEXP)        = { "(" }
FIRST(FORM)        = { "(", "int", "real", "memid" }
FIRST(TAIL1)       = { "(", "int", "real", "memid", "res", "v", ε }
FIRST(TAIL2)       = { "+", "-", "*", "|", "/", "%", "^", 
                       ">", "<", ">=", "<=", "==", "!=",
                       "(", "int", "real", "memid", "while" }
FIRST(STACKTERM)   = { "(", "int", "real", "memid" }
FIRST(VALUE)       = { "int", "real", "memid" }
FIRST(OP)          = { "+", "-", "*", "|", "/", "%", "^", 
                       ">", "<", ">=", "<=", "==", "!=" }
```

### Análise dos Conjuntos FIRST

- **PROGRAM** e **LINES**: Podem começar com `(` (uma linha) ou serem vazios (ε)
- **SEXP**: Sempre começa com `(`
- **FORM**: Começa com qualquer valor ou sub-expressão
- **TAIL1**: Pode ser um segundo operando, comando especial (res, v) ou vazio
- **TAIL2**: Pode ser um operador ou estrutura de controle
- **VALUE**: Qualquer tipo de valor literal

## 3. CONJUNTOS FOLLOW

Os conjuntos FOLLOW indicam quais terminais podem aparecer imediatamente após cada não-terminal.

```
FOLLOW(PROGRAM)    = { "$" }
FOLLOW(LINES)      = { "$" }
FOLLOW(LINE)       = { "(", "$" }
FOLLOW(SEXP)       = { "(", ")", "$", 
                       "+", "-", "*", "|", "/", "%", "^",
                       ">", "<", ">=", "<=", "==", "!=",
                       "int", "real", "memid",
                       "res", "v", "if", "while" }
FOLLOW(FORM)       = { ")" }
FOLLOW(TAIL1)      = { ")" }
FOLLOW(TAIL2)      = { ")" }
FOLLOW(STACKTERM)  = { "(", ")", "$",
                       "+", "-", "*", "|", "/", "%", "^",
                       ">", "<", ">=", "<=", "==", "!=",
                       "int", "real", "memid",
                       "res", "v", "if", "while" }
FOLLOW(VALUE)      = { "(", ")", "$",
                       "+", "-", "*", "|", "/", "%", "^",
                       ">", "<", ">=", "<=", "==", "!=",
                       "int", "real", "memid",
                       "res", "v", "if", "while" }
FOLLOW(OP)         = { ")" }
```

### Análise dos Conjuntos FOLLOW

- **PROGRAM**: Seguido apenas por fim de arquivo ($)
- **FORM**, **TAIL1**, **TAIL2**, **OP**: Sempre fecham com `)`
- **SEXP**, **STACKTERM**, **VALUE**: Podem ser seguidos por praticamente qualquer token, pois podem aparecer em diversas posições

## 4. TABELA DE ANÁLISE LL(1)

A tabela LL(1) mapeia pares (Não-Terminal, Terminal lookahead) para produções.

### PROGRAM

| Lookahead | Produção |
|-----------|----------|
| `(` | PROGRAM → LINES |
| `$` | PROGRAM → ε |

### LINES

| Lookahead | Produção |
|-----------|----------|
| `(` | LINES → LINE LINES |
| `$` | LINES → ε |

### LINE

| Lookahead | Produção |
|-----------|----------|
| `(` | LINE → SEXP |

### SEXP

| Lookahead | Produção |
|-----------|----------|
| `(` | SEXP → ( FORM ) |

### FORM

| Lookahead | Produção |
|-----------|----------|
| `(`, `int`, `real`, `memid` | FORM → STACKTERM TAIL1 |

### TAIL1

| Lookahead | Produção |
|-----------|----------|
| `(`, `int`, `real`, `memid` | TAIL1 → STACKTERM TAIL2 |
| `res` | TAIL1 → res |
| `v` | TAIL1 → v memid |
| `)` | TAIL1 → ε |

### TAIL2

| Lookahead | Produção |
|-----------|----------|
| `+`, `-`, `*`, `\|`, `/`, `%`, `^` | TAIL2 → OP |
| `>`, `<`, `>=`, `<=`, `==`, `!=` | TAIL2 → OP |
| `(`, `int`, `real`, `memid` | TAIL2 → STACKTERM if |
| `while` | TAIL2 → while |

### STACKTERM

| Lookahead | Produção |
|-----------|----------|
| `(` | STACKTERM → SEXP |
| `int`, `real`, `memid` | STACKTERM → VALUE |

### VALUE

| Lookahead | Produção |
|-----------|----------|
| `int` | VALUE → int |
| `real` | VALUE → real |
| `memid` | VALUE → memid |

### OP

| Lookahead | Produção |
|-----------|----------|
| `+` | OP → + |
| `-` | OP → - |
| `*` | OP → * |
| `\|` | OP → \| |
| `/` | OP → / |
| `%` | OP → % |
| `^` | OP → ^ |
| `>` | OP → > |
| `<` | OP → < |
| `>=` | OP → >= |
| `<=` | OP → <= |
| `==` | OP → == |
| `!=` | OP → != |

### Propriedades da Tabela

- **Total de entradas**: 55
- **Conflitos**: 0 (gramática é LL(1))
- **Determinística**: Sim, cada par (não-terminal, terminal) mapeia para no máximo uma produção

## 5. EXEMPLO DE ÁRVORE SINTÁTICA

### Expressão de Entrada
```
( 10 8 + )
```

### Tokens Normalizados
```
[ "(", "int", "int", "+", ")", "$" ]
```

### Derivação (Produções Aplicadas)
```
1.  PROGRAM      → LINES
2.  LINES        → LINE LINES
3.  LINE         → SEXP
4.  SEXP         → ( FORM )
5.  FORM         → STACKTERM TAIL1
6.  STACKTERM    → VALUE
7.  VALUE        → int
8.  TAIL1        → STACKTERM TAIL2
9.  STACKTERM    → VALUE
10. VALUE        → int
11. TAIL2        → OP
12. OP           → +
13. LINES        → ε
```

### Árvore Sintática (Visualização ASCII)

```
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
```

### Interpretação

A árvore mostra a estrutura hierárquica da expressão RPN `( 10 8 + )`:
- O **PROGRAM** contém uma lista de **LINES**
- Há uma **LINE** seguida de **LINES** vazio (ε)
- A **LINE** contém uma **SEXP** (S-Expression)
- A **SEXP** é delimitada por `(` e `)`
- O **FORM** interno contém:
  - Um **STACKTERM** (primeiro operando: 10)
  - Um **TAIL1** que continua com:
    - Outro **STACKTERM** (segundo operando: 8)
    - Um **TAIL2** contendo o **OP** (operador: +)

Isso representa corretamente a operação `10 + 8` em notação RPN.

## 6. EXEMPLO DE ESTRUTURA IF

### Expressão de Entrada
```
( ( A B > ) ( X ) ( Y ) if )
```

### Tokens Normalizados
```
[ "(", "(", "memid", "memid", ">", ")", "(", "memid", ")", "(", "memid", ")", "if", ")", "$" ]
```

### Interpretação
- **Condição**: `( A B > )` - testa se A > B
- **Then branch**: `( X )` - retorna X se verdadeiro
- **Else branch**: `( Y )` - retorna Y se falso
- **Keyword**: `if` - indica estrutura condicional

### Estrutura na Gramática
```
TAIL2 → STACKTERM if
```
Onde STACKTERM antes de 'if' contém a then-branch, e STACKTERM na posição anterior (em TAIL1) pode conter a else-branch.

## 7. EXEMPLO DE ESTRUTURA WHILE

### Expressão de Entrada
```
( ( I N < ) ( ( I 1 + ) v I ) while )
```

### Tokens Normalizados
```
[ "(", "(", "memid", "memid", "<", ")", "(", "(", "memid", "int", "+", ")", "v", "memid", ")", "while", ")", "$" ]
```

### Interpretação
- **Condição**: `( I N < )` - testa se I < N
- **Corpo**: `( ( I 1 + ) v I )` - incrementa I (I = I + 1)
- **Keyword**: `while` - indica laço de repetição

### Estrutura na Gramática
```
TAIL2 → while
```

**Nota**: A gramática atual tem limitações para aceitar estruturas WHILE e IF com corpos complexos que envolvem operações de memória (v).

## 8. ESTATÍSTICAS DA GRAMÁTICA

- **Não-terminais**: 10
  - PROGRAM, LINES, LINE, SEXP, FORM, TAIL1, TAIL2, STACKTERM, VALUE, OP

- **Terminais**: 23 (incluindo $)
  - Literais: int, real, memid
  - Operadores aritméticos: +, -, *, |, /, %, ^
  - Operadores relacionais: >, <, >=, <=, ==, !=
  - Keywords: res, v, if, while
  - Delimitadores: (, )
  - Fim: $

- **Produções**: 31
  - Distribuídas pelos 10 não-terminais

- **Entradas na Tabela LL(1)**: 55
  - Todas as entradas são determinísticas

- **Propriedade LL(1)**: ✓ Verificada
  - Sem conflitos shift-reduce
  - Sem conflitos reduce-reduce
  - Cada célula da tabela contém no máximo uma produção

## 9. COMPLEXIDADE DOS ALGORITMOS

### Cálculo de FIRST
- **Complexidade**: O(|N| × |P| × |α|)
  - |N| = número de não-terminais
  - |P| = número de produções
  - |α| = tamanho médio das produções
- **Implementação**: Iterativa com ponto fixo
- **Número de iterações**: Depende da recursividade da gramática (tipicamente < 10)

### Cálculo de FOLLOW
- **Complexidade**: O(|N|² × |P| × |α|)
- **Implementação**: Iterativa com propagação
- **Dependência**: Requer conjuntos FIRST previamente calculados

### Construção da Tabela LL(1)
- **Complexidade**: O(|P| × |α| × |T|)
  - |T| = número de terminais
- **Verificação de conflitos**: O(|N| × |T|)

### Parser
- **Complexidade de parsing**: O(|tokens|)
  - Linear no tamanho da entrada
- **Espaço (pilha)**: O(profundidade da árvore)
  - Proporcional ao aninhamento máximo

## 10. LIMITAÇÕES CONHECIDAS

1. **Estruturas de controle complexas**: A gramática atual não aceita corpos de IF/WHILE que contenham operações de store (v) seguidas de operadores, causando 9 falhas de teste.

2. **Aninhamento**: Embora suporte aninhamento ilimitado de expressões aritméticas, há limitações nas estruturas de controle.

3. **Recuperação de erros**: O parser para na primeira erro sintático sem tentar recuperação.

## 11. VERIFICAÇÃO DA PROPRIEDADE LL(1)

Uma gramática é LL(1) se satisfaz:

### Condição 1: Produções Alternativas
Para toda produção A → α₁ | α₂ | ... | αₙ:
```
FIRST(αᵢ) ∩ FIRST(αⱼ) = ∅, para i ≠ j
```
✓ **Verificado**: Não há interseção entre FIRST das produções alternativas

### Condição 2: Produções com ε
Se A → ε, então:
```
FIRST(A) ∩ FOLLOW(A) = ∅
```
✓ **Verificado**: Para LINES, TAIL1 e PROGRAM que têm produções ε

### Resultado
**A gramática É LL(1)** - Confirmado pela construção da tabela sem conflitos.

---

*Documento gerado automaticamente pelo analisador sintático RA2_6*  
*Disciplina: Compiladores*  
*Fase 2: Análise Sintática*
