from argparse import ArgumentParser
from regex import createToken
from Processing import readGrammar
from Convert import CFGtoCNF
from Parser import CYKParse

if __name__ == "__main__":
    argParser = ArgumentParser()
    argParser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argParser.parse_args()

    # print(createToken(args.nama_file))
    
    # print(readGrammar("grammar.txt"))

    # print(CFGtoCNF(readGrammar("grammar.txt")))

    if CYKParse(CFGtoCNF(readGrammar("grammar.txt")), createToken(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")

    # print(readGrammar("grammar_test.txt"))

    # print(CFGtoCNF(readGrammar("grammar_test.txt")))

    # file = open(args.nama_file, "r")
    # if CYK_parse(CFGtoCNF(readGrammar("grammar_test.txt")), file.read()):
    #     print("ACCEPTED")
    # else:
    #     print("SYNTAX ERROR")
    # file.close()