def readGrammar(namaFile):
    file = open(namaFile, "r")
    CFG = {}

    row = file.readline()
    while row != "":
        head, body = row.replace("\n", "").split(" -> ")
        
        if head not in CFG.keys():
            CFG[head] = [body.split(" ")]
        else:
            CFG[head].append(body.split(" "))

        row = file.readline()

    file.close()

    return CFG

def isTerminal(string):
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
        "RETURN"
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
        "CHARACTER"
    ]
    
    return string in list_of_terminal

def isVariables(string):
    return not isTerminal(string)
