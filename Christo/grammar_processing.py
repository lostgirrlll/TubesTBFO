# ATURAN MENULIS GRAMMAR:
# Head pertama akan menjadi Start Symbol
# Tidak mengandung Useless Production (tidak terdapat Variables yang tidak dapat diderivasi menjadi string dan tidak terdapat Productions yang tidak muncul pada derivasi string)
# Tidak mengandung Null Production (tidak terdapat Variables yang menghasilkan epsilon, kecuali pada Start Symbol)

def read_grammar(nama_file):
    file = open(nama_file, "r")
    cfg = {}

    baris = file.readline()
    while baris != "":
        head, body = baris.replace("\n", "").split(" -> ")
        
        if head not in cfg.keys():
            cfg[head] = [body.split(" ")]
        else:
            cfg[head].append(body.split(" "))

        baris = file.readline()

    file.close()

    return cfg

def is_terminal(string):
    list_of_terminal = [
        "EQASSIGN",
        "EQCOMPARE",
        "SEMICOLON",
        "COLON",
        "ADD",
        "SUBTRACT",
        "MULTIPLY",
        "DIVIDE",
        "MOD",
        "POW",
        "LESSEQ",
        "LESS",
        "GREATEREQ",
        "GREATER",
        "NEQ",
        "SUBTASSIGN",
        "MULASSIGN",
        "ADDASSIGN",
        "DIVASSIGN",
        "MODASSIGN",
        "POWASSIGN",
        "AND",
        "OR",
        "NOT",
        "IF",
        "ELSE",
        "ELIF",
        "WHILE",
        "FALSE",
        "TRUE",
        "NONE",
        "BREAK",
        "CONTINUE",
        "DEF",
        "FOR",
        "RETURN",
        "COMMA",
        "DOUBLE_QUOTE",
        "QUOTE",
        "OSB",
        "CSB",
        "OCB",
        "CCB",
        "ORB",
        "CRB",
        "INT",
        "STRING",
        "MULTILINE",
        "VARIABLE",
        "NEWLINE",
        "CONST",
        "CASE",
        "CATCH",
        "DEFAULT",
        "DELETE",
        "DO",
        "FINALLY",
        "FUNCTION",
        "LET",
        "SWITCH",
        "THROW",
        "TRY",
        "VAR",
        "COLON",
        "DOT",
        "CHARACTER",
        "INCREMENT",
        "DECREMENT"
    ]
    
    return string in list_of_terminal
11
def is_variables(string):
    return not is_terminal(string)

# def is_variables(string):
#     return len(string) > 0 and string[0].isupper()

# def is_terminal(string):
#     return not is_variables(string)