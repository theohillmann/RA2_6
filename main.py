# Integrantes do grupo (ordem alfabética):
# Theo Hillmann Luiz Coelho - theohillmann
#
# Nome do grupo no Canvas: RA2_6

import os
import json
from build_grammar.build_grammar import construirGramatica
from parsear.parsear import parsear
from ler_tokens.ler_tokens import lerTokens
from gerar_arvore.gerar_arvore import gerarArvore, print_tree


def tokens_to_expr_key(tokens):
    """Gera uma string legível da expressão (sem o marcador $)."""
    return " ".join(tokens[:-1]) if tokens and tokens[-1] == "$" else " ".join(tokens)


def main(tokens_path):

    all_exprs = lerTokens(tokens_path)
    if not all_exprs:
        print("Arquivo sem expressões.")
        return

    grammar = construirGramatica()
    table = grammar["table"]
    start = grammar["start"]

    trees_by_expr = {}
    ok = err = 0

    for i, tokens in enumerate(all_exprs, start=1):
        expr_key = tokens_to_expr_key(tokens)
        print(f"\n=== Expressão {i} ===")
        print("Tokens:", " ".join(tokens))

        try:
            deriv = parsear(tokens, table, debug=False)
            print(f"✅ Expressão aceita. Derivação com {len(deriv)} produções.")

            tree = gerarArvore(deriv, start_symbol=start)
            print("\nÁrvore sintática (ASCII):")
            print_tree(tree)

            key = expr_key
            if key in trees_by_expr:
                k = 2
                while f"{expr_key} #{k}" in trees_by_expr:
                    k += 1
                key = f"{expr_key} #{k}"
            trees_by_expr[key] = tree.to_dict()
            ok += 1

        except Exception as e:
            print("❌ Erro:", e)
            err += 1

    base, _ = os.path.splitext(tokens_path)
    output_path = base + ".json"

    with open(output_path, "w", encoding="utf-8") as fp:
        json.dump(trees_by_expr, fp, ensure_ascii=False, indent=2)

    print(f"\nResumo: {ok} aceitas, {err} com erro.")
    print(f"Árvores salvas em: {output_path}")


if __name__ == "__main__":
    import sys
    
    # Aceita arquivo por linha de comando ou usa padrão
    if len(sys.argv) > 1:
        f = sys.argv[1]
    else:
        print("Uso: python main.py <arquivo_tokens>")
        print("Usando arquivo padrão: tokens/test1.txt")
        f = "tokens/test1.txt"
    
    main(f)
