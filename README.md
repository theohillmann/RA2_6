# RA2_6

PROGRAM   = LINES ;

LINES     = LINE LINES | ε ;
LINE      = SEXP ;

SEXP      = "(" FORM ")" ;

FORM      = memid
          | STACKTERM TAIL1 ;

TAIL1     = STACKTERM TAIL2 
          | res            
          | memid ;

TAIL2     = OP
          | STACKTERM if
          | while ;

STACKTERM = VALUE
          | SEXP ;

VALUE     = int | real ;

OP        = "+" | "-" | "*" | "|" | "/" | "%" | "^" ;