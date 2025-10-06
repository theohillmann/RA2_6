# RELATÓRIO DE AVALIAÇÃO - ANALISADOR SINTÁTICO LL(1)

## IDENTIFICAÇÃO
- **Repositório**: theohillmann/RA2_6
- **Linguagem**: Python
- **Membros**: Theo Hillmann Luiz Coelho
- **Nome do Grupo**: RA2_6

## ANÁLISE DA GRAMÁTICA LL(1) (ELIMINATÓRIA)
- **Gramática LL(1) implementada**: **SIM**
- **Descrição da implementação encontrada**: O projeto implementa uma gramática LL(1) completa com funções bem definidas para construção da gramática (`construirGramatica()`), cálculo de conjuntos FIRST (`calcularFirst()`) e FOLLOW (`calcularFollow()`), e construção da tabela de parsing LL(1) (`construirTabelaLL1()`). O analisador sintático utiliza um parser descendente recursivo com pilha de análise, conforme especificado no enunciado.

---

## PONTUAÇÃO DETALHADA

### Funcionalidades do Analisador (70 pontos)

#### 1. Função `construirGramatica` e Análise LL(1): [18/20]
**Pontos Positivos:**
- ✓ Implementa `construirGramatica()` que retorna dicionário com gramática completa
- ✓ Calcula conjuntos FIRST para todos os não-terminais (arquivo `calcular_first.py`)
- ✓ Calcula conjuntos FOLLOW para todos os não-terminais (arquivo `calcular_follow.py`)
- ✓ Constrói tabela de análise LL(1) sem conflitos
- ✓ Validação de gramática LL(1) (detecta conflitos via exceções)
- ✓ Gramática definida em EBNF no arquivo `constants.py`
- ✓ Implementa algoritmos corretos para FIRST e FOLLOW
- ✓ Funções auxiliares bem implementadas (`get_first_of_sequence()`)

**Penalizações:**
- **-2 pontos**: Ausência de documentação formal dos conjuntos FIRST e FOLLOW em arquivo markdown separado (apenas implementados no código)

**Análise da Gramática:**
```
PROGRAM → LINES
LINES → LINE LINES | ε
LINE → SEXP
SEXP → ( FORM )
FORM → STACKTERM TAIL1
TAIL1 → STACKTERM TAIL2 | res | mem_store | ε
TAIL2 → OP | STACKTERM if | while
STACKTERM → VALUE | SEXP
VALUE → int | real | memid
OP → + | - | * | | | / | % | ^ | > | < | >= | <= | == | !=
```

A gramática está bem definida e é claramente LL(1) (sem conflitos na tabela).

#### 2. Função `parsear` e Parser Descendente Recursivo: [20/20]
**Pontos Positivos:**
- ✓ Implementa `parsear(tokens, ll1_table)` para análise sintática
- ✓ Usa tabela LL(1) para guiar o processo de parsing
- ✓ Implementa pilha de análise com controle de derivação
- ✓ Detecta e reporta erros sintáticos com mensagens claras e informativas
- ✓ Retorna lista de derivações (pares não-terminal, produção)
- ✓ Implementa algoritmo LL(1) com pilha corretamente
- ✓ Gerenciamento adequado do buffer de entrada de tokens
- ✓ Tratamento especial para produções epsilon
- ✓ Funções auxiliares bem organizadas (`handle_nonterminal`, `handle_terminal`, etc.)
- ✓ Testes unitários incluídos no próprio módulo (seção `if __name__ == "__main__"`)

**Mensagens de erro exemplares:**
- "Syntax error: unexpected symbol 'X' while expanding Y. Expected one of: [...]"
- "Error: expected terminal 'X', but found 'Y'. Input context: [...]"

#### 3. Função `lerTokens` e Estruturas de Controle: [17/20]
**Pontos Positivos:**
- ✓ Implementa `lerTokens(arquivo)` para ler tokens
- ✓ Define tokens para estruturas de decisão (`if`) e repetição (`while`)
- ✓ Adiciona operadores relacionais (`>`, `<`, `==`, `!=`, `>=`, `<=`)
- ✓ Validação de tokens implementada
- ✓ Normalização de lexemas para tokens da gramática
- ✓ Reconhece números inteiros e reais
- ✓ Reconhece identificadores de memória (variáveis)
- ✓ Implementa comando especial `mem_store` (para armazenar em variável)
- ✓ Tratamento de erros com indicação de linha

**Penalizações:**
- **-3 pontos**: Falta documentação clara da sintaxe das estruturas de controle. Embora implementadas na gramática, não há exemplos documentados de como usá-las de forma explícita em um arquivo markdown separado.

**Estruturas de Controle Implementadas:**
- **Decisão (if)**: `( condição then else if )` onde condição, then e else são SEXP
- **Repetição (while)**: `( condição corpo while )` onde condição e corpo são SEXP

#### 4. Função `gerarArvore`, Interface e Integração: [15/15]
**Pontos Positivos:**
- ✓ Implementa `gerarArvore(derivacao)` para construir árvore sintática
- ✓ Transforma derivação em estrutura de árvore
- ✓ Implementa impressão ASCII da árvore (`print_tree`)
- ✓ Salva árvore em formato JSON
- ✓ Implementa `main()` que integra todos os módulos
- ✓ Interface de linha de comando funcional
- ✓ Gerencia execução completa do fluxo
- ✓ Testes end-to-end funcionais
- ✓ Classe `Node` bem estruturada com método `to_dict()`
- ✓ Validação de consistência na construção da árvore

**Subtotal Funcionalidades:** 70/70

---

### Organização e Legibilidade do Código (15 pontos)

#### 1. Qualidade do Código: [5/5]
- ✓ Código muito bem comentado com docstrings detalhadas
- ✓ Funções bem definidas e organizadas em módulos separados
- ✓ Nomes de variáveis e funções muito claros e descritivos
- ✓ Tratamento de erros bem implementado com exceções customizadas
- ✓ Estrutura modular excelente (4 módulos bem separados)
- ✓ Type hints utilizados em vários lugares
- ✓ Código segue convenções Python (PEP 8)

**Organização de Módulos:**
```
build_grammar/    - Construção da gramática, FIRST, FOLLOW, tabela LL(1)
parsear/         - Analisador sintático
ler_tokens/      - Leitura e normalização de tokens
gerar_arvore/    - Geração e visualização da árvore sintática
```

#### 2. Documentação (README): [3/5]
**Pontos Positivos:**
- ✓ README.md presente e bem estruturado
- ✓ Instruções de execução claras
- ✓ Nomes dos alunos presentes no README
- ✓ Estrutura do projeto bem documentada
- ✓ Projeto desenvolvido para PUCPR mencionado

**Penalizações:**
- **-1 ponto**: Falta nome completo da instituição (apenas "PUCPR")
- **-1 ponto**: Falta informações sobre o professor e disciplina completos
- **-0 pontos**: Instruções de compilação não aplicáveis (Python não precisa compilação)

#### 3. Repositório GitHub: [5/5]
- ✓ Arquivos de teste presentes (test1.txt, test2.txt, test3.txt)
- ✓ Arquivos JSON de saída gerados (test1.json, test2.json, test3.json)
- ✓ Estrutura muito bem organizada
- ✓ .gitignore adequado
- ✓ Commits com mensagens claras
- ✓ Repositório público conforme solicitado

**Subtotal Organização:** 13/15

---

### Robustez (15 pontos)

#### 1. Arquivos de Teste Adequados: [5/8]
**Pontos Positivos:**
- ✓ 3 arquivos de teste presentes (test1.txt, test2.txt, test3.txt)
- ✓ test1.txt contém todas as operações: +, -, *, |, /, %, ^
- ✓ Comandos especiais testados: RES, MEM
- ✓ test2.txt contém estrutura de decisão (if)
- ✓ test3.txt contém estrutura de repetição (while)
- ✓ Uso de inteiros e reais
- ✓ Uso de memórias (variáveis)

**Penalizações:**
- **-2 pontos**: test2.txt tem apenas 8 linhas (requisito mínimo: 10 linhas)
- **-1 ponto**: test3.txt tem apenas 7 linhas (requisito mínimo: 10 linhas)
- **-0 pontos**: test1.txt tem 12 linhas (✓ atende)

**Observação Importante**: O enunciado especifica "mínimo de 3 arquivos com pelo menos 10 linhas cada". Apenas test1.txt atende este requisito completamente.

#### 2. Tratamento de Erros no Código: [7/7]
**Pontos Positivos:**
- ✓ Tratamento completo de erros sintáticos
- ✓ Exceção customizada `SyntaxErrorLL1`
- ✓ Validação de tokens inválidos em `lerTokens`
- ✓ Mensagens de erro muito descritivas com contexto
- ✓ Validação de parenteses (implícita na gramática)
- ✓ Tratamento de tokens inesperados
- ✓ Validação de consistência na construção da árvore
- ✓ Erro com indicação de linha no arquivo de entrada

**Exemplos de Tratamento:**
```python
raise SyntaxErrorLL1(
    f"Syntax error: unexpected symbol '{current_token}' while expanding {stack_top}. "
    f"Expected one of: {expected_tokens}"
)
```

**Subtotal Robustez:** 12/15

---

## PROBLEMAS ENCONTRADOS

### Problemas Críticos
- **NENHUM PROBLEMA CRÍTICO**: O analisador sintático funciona corretamente.

### Problemas Moderados
1. **Documentação Incompleta da Gramática (-2 pontos)**:
   - Não há arquivo markdown separado documentando formalmente:
     * Regras de produção em formato EBNF
     * Conjuntos FIRST calculados
     * Conjuntos FOLLOW calculados
     * Tabela de Análise LL(1)
   - Estas informações existem apenas no código, mas o enunciado especifica: "Arquivo markdown com a gramática, conjuntos FIRST/FOLLOW, tabela LL(1) e a árvore sintática da última execução"

2. **Arquivos de Teste Insuficientes (-3 pontos)**:
   - test2.txt: 8 linhas (faltam 2 linhas para atingir mínimo de 10)
   - test3.txt: 7 linhas (faltam 3 linhas para atingir mínimo de 10)

3. **Documentação das Estruturas de Controle (-3 pontos)**:
   - Falta documentação explícita da sintaxe do if e while no README
   - Não há exemplos detalhados de uso das estruturas de controle

### Problemas Menores
1. **Falta de Informações Institucionais Completas (-2 pontos)**:
   - Nome completo da instituição não especificado
   - Nome do professor não mencionado
   - Nome completo da disciplina não especificado

2. **Ausência de Comentários de Identificação no Código**:
   - Os arquivos .py não contêm no cabeçalho as informações dos integrantes conforme especificado:
   ```python
   // Integrantes do grupo (ordem alfabética):
   // Nome Completo 1 - username1
   // Nome Completo 2 - username2
   //
   // Nome do grupo no Canvas: [Nome do Grupo]
   ```

### Pontos Positivos Destacados
1. **Implementação Técnica Excelente**:
   - Parser LL(1) perfeitamente implementado
   - Algoritmos de FIRST e FOLLOW corretos
   - Gramática bem projetada e livre de conflitos
   - Código muito limpo e bem estruturado

2. **Estrutura Modular Exemplar**:
   - Separação clara de responsabilidades
   - Cada módulo com sua função específica
   - Fácil manutenção e extensão

3. **Tratamento de Erros Robusto**:
   - Mensagens muito informativas
   - Contexto adequado nos erros
   - Exceções personalizadas

4. **Interface Profissional**:
   - Linha de comando bem implementada
   - Saída formatada e legível
   - Árvore sintática em ASCII muito clara

---

## NOTA FINAL: 95/100

### Distribuição da Nota:
- **Funcionalidades (70 pontos)**: 70/70
- **Organização (15 pontos)**: 13/15
- **Robustez (15 pontos)**: 12/15

---

## ANÁLISE DOS ARQUIVOS DE TESTE

### test1.txt (12 linhas) ✓
**Conteúdo**: Expressões aritméticas básicas
- ✓ Operações: +, -, *, /, %, ^ (todas presentes)
- ✓ Comando RES presente
- ✓ Comando MEM presente
- ✓ Números inteiros e variáveis
- ✓ Expressões aninhadas
- **Status**: COMPLETO

### test2.txt (8 linhas) ⚠
**Conteúdo**: Estrutura de decisão (if)
- ✓ Estrutura de decisão implementada
- ✓ Operadores relacionais (>, ==)
- ✓ Expressões aninhadas
- ⚠ **Problema**: Apenas 8 linhas (faltam 2)
- **Status**: INCOMPLETO (não atinge mínimo de 10 linhas)

### test3.txt (7 linhas) ⚠
**Conteúdo**: Estrutura de repetição (while)
- ✓ Estrutura de repetição implementada
- ✓ Operador relacional (<)
- ✓ Uso de variáveis
- ⚠ **Problema**: Apenas 7 linhas (faltam 3)
- **Status**: INCOMPLETO (não atinge mínimo de 10 linhas)

---

## GRAMÁTICA IMPLEMENTADA

### Não-Terminais
```
PROGRAM, LINES, LINE, SEXP, FORM, TAIL1, TAIL2, STACKTERM, VALUE, OP
```

### Terminais
```
(, ), int, real, memid, mem_store, res, if, while
+, -, *, |, /, %, ^, >, <, >=, <=, ==, !=, $
```

### Produções (Formato Simplificado)
```
1.  PROGRAM → LINES
2.  LINES → LINE LINES | ε
3.  LINE → SEXP
4.  SEXP → ( FORM )
5.  FORM → STACKTERM TAIL1
6.  TAIL1 → STACKTERM TAIL2 | res | mem_store | ε
7.  TAIL2 → OP | STACKTERM if | while
8.  STACKTERM → VALUE | SEXP
9.  VALUE → int | real | memid
10. OP → + | - | * | | | / | % | ^ | > | < | >= | <= | == | !=
```

**Observação**: A gramática está corretamente implementada e é LL(1).

---

## ÁRVORE SINTÁTICA

As árvores sintáticas são geradas corretamente e salvas em formato JSON para cada arquivo de teste:
- `tokens/test1.json` ✓
- `tokens/test2.json` ✓
- `tokens/test3.json` ✓

**Exemplo de Visualização (ASCII):**
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

---

## OBSERVAÇÕES FINAIS

Este trabalho representa uma **excelente implementação** de um analisador sintático LL(1). O projeto demonstra:

### Pontos Fortes:
1. ✓ Parser LL(1) perfeitamente implementado com pilha
2. ✓ Algoritmos FIRST e FOLLOW corretos
3. ✓ Gramática bem projetada (sem conflitos)
4. ✓ Código muito limpo e bem organizado
5. ✓ Estrutura modular exemplar
6. ✓ Tratamento de erros robusto
7. ✓ Árvore sintática bem gerada
8. ✓ Interface profissional
9. ✓ Estruturas de controle (if/while) implementadas

### Melhorias Necessárias:
1. ❌ Criar arquivo markdown formal com:
   - Gramática completa em EBNF
   - Conjuntos FIRST de todos os não-terminais
   - Conjuntos FOLLOW de todos os não-terminais
   - Tabela de Análise LL(1) completa
2. ❌ Adicionar mais linhas aos arquivos test2.txt e test3.txt (mínimo 10 linhas cada)
3. ❌ Documentar sintaxe das estruturas de controle no README com exemplos
4. ❌ Adicionar cabeçalho com informações dos integrantes nos arquivos .py
5. ❌ Completar informações institucionais no README

### Conclusão:
O trabalho está **muito bem implementado tecnicamente**, com código de qualidade profissional. Os principais problemas são de **documentação e formato**, não de funcionalidade. Com as melhorias sugeridas, este projeto pode alcançar nota máxima.

A implementação demonstra domínio completo dos conceitos de análise sintática LL(1), construção de gramáticas, cálculo de conjuntos FIRST/FOLLOW e geração de árvores sintáticas.

---

**Data da Avaliação**: 2024  
**Avaliador**: Sistema Automatizado de Avaliação de Projetos de Compiladores
