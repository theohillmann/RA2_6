from typing import List
from build_grammar.constants import END

VALID_SINGLE_TOKENS = {
    "(",
    ")",
    "res",
    "v",
    "if",
    "while",
    "+",
    "-",
    "*",
    "|",
    "/",
    "%",
    "^",
    ">",
    "<",
    ">=",
    "<=",
    "==",
    "!=",
}


def read_tokens(input_file: str) -> List[List[str]]:
    """
    Reads a file with ONE EXPRESSION PER LINE and returns
    a list of normalized token vectors (each ends with '$').
    """
    tokenized_lines: List[List[str]] = []
    with open(input_file, "r", encoding="utf-8") as file:
        for line_number, current_line in enumerate(file, start=1):
            current_line = current_line.strip()
            if not current_line:
                continue
            try:
                tokenized_lines.append(_normalize_line_to_tokens(current_line))
            except ValueError as error:
                raise ValueError(f"[line {line_number}] {error}")
    return tokenized_lines


def _normalize_line_to_tokens(input_line: str) -> List[str]:
    line_parts = [part for part in input_line.strip().split() if part]
    if not line_parts:
        return [END]
    tokens = [_normalize_lexeme_to_token(part) for part in line_parts]
    tokens.append(END)
    return tokens


def _normalize_lexeme_to_token(lexeme: str) -> str:
    """
    Converts a raw lexeme to the grammar terminal (without regex):
      - numbers → "int"/"real"
      - keywords (case-insensitive) → "res" | "v" | "if" | "while"
      - parentheses/operators (incl. relational) → as they are (if valid)
      - identifiers → "memid"
    """
    cleaned_lexeme = lexeme.strip()
    if not cleaned_lexeme:
        raise ValueError("empty lexeme")

    keyword = cleaned_lexeme.lower()
    if keyword in {"res", "v", "if", "while"}:
        return keyword

    if cleaned_lexeme in VALID_SINGLE_TOKENS:
        return cleaned_lexeme

    if _is_integer_lexeme(cleaned_lexeme):
        return "int"
    if _is_real_number_lexeme(cleaned_lexeme):
        return "real"

    if _is_memory_identifier_lexeme(cleaned_lexeme):
        return "memid"

    raise ValueError(f"Invalid/unsupported lexeme: '{lexeme}'")


def _is_sign(character: str) -> bool:
    return character in "+-"


def _is_integer_lexeme(text: str) -> bool:
    if not text:
        return False
    start_index = 1 if _is_sign(text[0]) and len(text) > 1 else 0
    if start_index == len(text):
        return False
    return all(char.isdigit() for char in text[start_index:])


def _is_real_number_lexeme(text: str) -> bool:
    if not text:
        return False
    start_index = 1 if _is_sign(text[0]) and len(text) > 1 else 0
    number_part = text[start_index:]
    if number_part.count(".") != 1:
        return False
    integer_part, decimal_part = number_part.split(".", 1)
    if not integer_part or not decimal_part:
        return False
    return integer_part.isdigit() and decimal_part.isdigit()


def _is_memory_identifier_lexeme(text: str) -> bool:
    if not text or not text[0].isalpha():
        return False
    for character in text[1:]:
        if not (character.isalnum() or character == "_"):
            return False
    return True


if __name__ == "__main__":
    input_file_path = "/Users/theocoelho/Documents/academico/faculdade/10 periodo/compiladores/RA2_6/tokens/tokens.txt"
    print(read_tokens(input_file_path))
