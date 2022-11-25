import sys
import re

token_exp = [

(r'[ \t]+',                 None),
(r'#[^\n]*',                None),
(r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',  None),
(r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',  None), 

# integer and string
(r'\"[^\"\n]*\"',           "STRING"),
(r'\'[^\'\n]*\'',           "STRING"),
(r'[\+\-]?[0-9]*\.[0-9]+',  "INT"),
(r'[\+\-]?[1-9][0-9]+',     "INT"),
(r'[\+\-]?[0-9]',           "INT"),

# operator
(r'\*\*=',                  "POWASSIGN"),
(r'\*\*',                   "POW"),
(r'\*=',                    "MULASSIGN"),
(r'/=',                     "DIVASSIGN"),
(r'\+=',                    "ADDASSIGN"),
(r'-=',                     "SUBASSIGN"),
(r'%=',                     "MODASSIGN"),
(r'\+',                     "ADD"),
(r'\-',                     "SUBTRACT"),
(r'\*',                     "MULTIPLY"),
(r'/',                      "DIVIDE"),
(r'%',                      "MOD"),
(r'<=',                     "LESSEQ"),
(r'<',                      "LESS"),
(r'>=',                     "GREATEREQ"),
(r'>',                      "GREATER"),
(r'!=',                     "NEQ"),
(r'\==',                    "EQCOMPARE"),
(r'\=(?!\=)',               "EQASSIGN"),
(r'\&\&',                   "AND"),
(r'\|\|',                   "OR"),
(r'\!',                     "NOT"),
(r'\+\+',                   "INCREMENT"),
(r'\-\-',                   "DECREMENT"),


# Delimiter
(r'\(',                 "ORB"),
(r'\)',                 "CRB"),
(r'\[',                 "OSB"),
(r'\]',                 "CSB"),
(r'\{',                 "OCB"),
(r'\}',                 "CCB"),
(r'\,',                 "COMMA"),
(r'\:',                 "COLON"),
(r'\;',                 "SEMICOLON"),
(r'\.',                 "DOT"),
(r'\n',                 "NEWLINE"),

# Keyword
(r'\bif\b',             "IF"),
(r'\belse\b',           "ELSE"),
(r'\belse\b',           "ELSE"),
(r'\bwhile\b',          "WHILE"),
(r'\bfor\b',            "FOR"),
(r'\breturn\b',         "RETURN"),
(r'\brange\b',          "RANGE"),
(r'\bbreak\b',          "BREAK"),
(r'\bcase\b',           "CASE"),
(r'\bcatch\b',          "CATCH"),
(r'\bdefault\b',        "DEFAULT"),
(r'\bcontinue\b',       "CONTINUE"),
(r'\bfunction\b',       "FUNCTION"),
(r'\bvar\b',            "VAR"),
(r'\bconst\b',          "CONST"),
(r'\blet\b',            "LET"),
(r'\bdelete\b',         "DELETE"),
(r'\bdefault\b',        "DEFAULT"),
(r'\bdo\b',             "DO"),
(r'\bfinally\b',        "FINALLY"),
(r'\bswitch\b',         "SWITCH"),
(r'\bthrow\b',          "THROW"),
(r'\btry\b',            "TRY"),
(r'\bimport\b',         "IMPORT"),
(r'\bset\b',            "SET"),
(r'\band\b',            "AND"),
(r'\bor\b',             "OR"),
(r'\bnot\b',            "NOT"),
(r'\bthen\b',           "THEN"),
(r'\bfalse\b',          "FALSE"),
(r'\btrue\b',           "TRUE"),
(r'\bnull\b',           "NULL"),
(r'\bdef\b',            "DEF"),
(r'\bas\b',             "AS"),
(r'\bfrom\b',           "FROM"),
(r'\bint\b',            "INT"),
(r'\bstring\b',         "STRING"),
(r'\bfloat\b',          "FLOAT"),
(r'\bboolean\b',        "BOOL"),
(r'\blist\b',           "STATIC"),
(r'\bchar\b',           "STRING"),
(r'\bvar\b',            "VAR"),
(r'\'\'\'[(?!(\'\'\'))\w\W]*\'\'\'',       "MULTILINE"),
(r'\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"',       "MULTILINE"),
(r'[A-Za-z_][A-Za-z0-9_]*', "VARIABLE"),

]

# teks ke token
newA = r'[\n]+[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
newB = r'[\n]+[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'

def lexer(teks, token_exp):
    pos = 0 # posisi karakter pada seluruh potongan teks (absolut)
    cur = 1 # posisi karakter relatif terhadap baris tempat dia berada
    line = 1 # posisi baris saat ini
    tokens = []
    while pos < len(teks):
        if teks[pos] == '\n':
            cur = 1
            line += 1
        match = None

        for t in token_exp:
            pattern, tag = t
            if line == 1:
                if pattern == newA:
                    pattern = r'[^\w]*[ \t]*\'\'\'[(?!(\'\'\'))\w\W]*\'\'\''
                elif pattern == newB:
                    pattern = r'[^\w]*[ \t]*\"\"\"[(?!(\"\"\"))\w\W]*\"\"\"'
            regex = re.compile(pattern)
            match = regex.match(teks, pos)
            if match:
                if tag:
                    token = tag
                    tokens.append(token)
                break

        if not match:
            print("ILLEGAL CHARACTER")
            print("SYNTAX ERROR")
            sys.exit(1)
        else:
            pos = match.end(0)
        cur += 1
    return tokens

def create_token(sentence):
    file = open(sentence)
    char = file.read()
    file.close()

    tokens = lexer(char,token_exp)
    tokenArray = []
    for token in tokens:
        tokenArray.append(token)

    return " ".join(tokenArray)

if __name__ == "__main__":
    create_token('test.txt')

