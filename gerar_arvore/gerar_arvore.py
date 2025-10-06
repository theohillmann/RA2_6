from typing import List, Dict, Any

EPS = "ε"


class Node:
    def __init__(self, label: str):
        self.label: str = label
        self.children: List["Node"] = []

    def to_dict(self) -> Dict[str, Any]:
        if not self.children:
            return {"label": self.label}
        return {"label": self.label, "children": [c.to_dict() for c in self.children]}


def gerarArvore(derivacao: List[tuple], start_symbol: str) -> Node:
    """
    Reconstrói a árvore sintática a partir da derivação (lista de produções aplicadas).
    Estratégia:
      - Mantemos uma pilha de nós "a expandir".
      - Começa com o nó raiz (start_symbol).
      - Para cada produção (A -> α) na derivação:
          * o topo da pilha deve ser A; removemos da pilha
          * criamos filhos para cada símbolo em α (na ordem)
          * empilhamos, em ordem inversa, apenas os NÃO-TERMINAIS (para futuras expansões)
        Observação: folhas terminais são criadas aqui como nós com rótulo do próprio terminal.
        Produções ε não geram filhos.
    """
    if not derivacao:
        raise ValueError("Derivação vazia.")

    root = Node(start_symbol)
    stack: List[Node] = [root]

    for lhs, rhs in derivacao:
        if not stack:
            raise ValueError(f"Pilhas esgotadas antes de expandir {lhs} -> {rhs}")
        current = stack.pop()

        if current.label != lhs:
            raise ValueError(
                f"Inconsistência na derivação: topo='{current.label}', produção para='{lhs}'."
            )

        if len(rhs) == 1 and rhs[0] == EPS:
            continue

        children = [Node(sym) for sym in rhs]
        current.children.extend(children)

        lhs_set = {A for (A, _) in derivacao}

        for child in reversed(children):
            if child.label in lhs_set:
                stack.append(child)

    if any(n.label in {A for (A, _) in derivacao} for n in stack):
        raise ValueError("Sobrou não-terminal para expandir ao final da derivação.")

    return root


def print_tree(node: Node, indent: str = "", is_last: bool = True) -> None:
    """
    Impressão ASCII da árvore:
      └─ SEXP
         ├─ (
         ├─ FORM
         │  └─ ...
         └─ )
    """
    connector = "└─ " if is_last else "├─ "
    print(indent + connector + node.label)
    new_indent = indent + ("   " if is_last else "│  ")
    for i, child in enumerate(node.children):
        last = i == len(node.children) - 1
        print_tree(child, new_indent, last)


if __name__ == "__main__":
    derivacao = [
        ("PROGRAM", ["LINES"]),
        ("LINES", ["LINE", "LINES"]),
        ("LINE", ["SEXP"]),
        ("SEXP", ["(", "FORM", ")"]),
        ("FORM", ["STACKTERM", "TAIL1"]),
        # --- cond: ( A B > )
        ("STACKTERM", ["SEXP"]),
        ("SEXP", ["(", "FORM", ")"]),
        ("FORM", ["STACKTERM", "TAIL1"]),
        ("STACKTERM", ["VALUE"]),
        ("VALUE", ["memid"]),  # A
        ("TAIL1", ["STACKTERM", "TAIL2"]),
        ("STACKTERM", ["VALUE"]),
        ("VALUE", ["memid"]),  # B
        ("TAIL2", ["OP"]),
        ("OP", [">"]),
        # --- TAIL1 externo escolhe STACKTERM TAIL2 (há then/else)
        ("TAIL1", ["STACKTERM", "TAIL2"]),
        # --- then: ( ( A B + ) v R )
        ("STACKTERM", ["SEXP"]),
        ("SEXP", ["(", "FORM", ")"]),
        ("FORM", ["STACKTERM", "TAIL1"]),
        ("STACKTERM", ["SEXP"]),
        ("SEXP", ["(", "FORM", ")"]),
        ("FORM", ["STACKTERM", "TAIL1"]),
        ("STACKTERM", ["VALUE"]),
        ("VALUE", ["memid"]),  # A
        ("TAIL1", ["STACKTERM", "TAIL2"]),
        ("STACKTERM", ["VALUE"]),
        ("VALUE", ["memid"]),  # B
        ("TAIL2", ["OP"]),
        ("OP", ["+"]),
        ("TAIL1", ["v", "memid"]),  # v R
        # --- TAIL2 externo escolhe STACKTERM if  (else + 'if')
        ("TAIL2", ["STACKTERM", "if"]),
        # --- else: ( 0 v R )
        ("STACKTERM", ["SEXP"]),
        ("SEXP", ["(", "FORM", ")"]),
        ("FORM", ["STACKTERM", "TAIL1"]),
        ("STACKTERM", ["VALUE"]),
        ("VALUE", ["int"]),  # 0
        ("TAIL1", ["v", "memid"]),  # v R
        # --- fim das linhas
        ("LINES", ["ε"]),
    ]
    tree = gerarArvore(derivacao, start_symbol="PROGRAM")
    print_tree(tree)
