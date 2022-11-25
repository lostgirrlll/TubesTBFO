from argparse import ArgumentParser
from file_processing import create_token
from grammar_processing import read_grammar
from grammar_convert import CFG_to_CNF
from grammar_parser import CYK_parse

if __name__ == "__main__":
    argument_parser = ArgumentParser()
    argument_parser.add_argument("nama_file", type=str, help="Nama File yang hendak diparse.")

    args = argument_parser.parse_args()

    # print(create_token(args.nama_file))
    
    # X = (read_grammar("grammar.txt"))
    # for k, d in X.items():
    #     print(k + ":", d) 

    # Y = CFG_to_CNF(read_grammar("grammar.txt"))
    # for k, d in Y.items():
    #     print(k + ":", d) 

    if CYK_parse(CFG_to_CNF(read_grammar("grammar.txt")), create_token(args.nama_file)):
        print("ACCEPTED")
    else:
        print("SYNTAX ERROR")

    # print(read_grammar("grammar_test.txt"))

    # print(CFG_to_CNF(read_grammar("grammar_test.txt")))

    # file = open(args.nama_file, "r")
    # if CYK_parse(CFG_to_CNF(read_grammar("grammar_test.txt")), file.read()):
    #     print("ACCEPTED")
    # else:
    #     print("SYNTAX ERROR")
    # file.close()