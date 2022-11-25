def CYKParse(CNF, input):
    S = input.split(" ")
    length = len(S)
    List = [[set([]) for j in range(length)] for i in range(length)]

    for j in range(length):
        for head, body in CNF.items():
            for rule in body:
                if len(rule) == 1 and rule[0] == S[j]:
                    List[j][j].add(head)

        for i in range(j, -1, -1):
            for k in range(i, j):
                for head, body in CNF.items():
                    for rule in body:
                        if len(rule) == 2 and rule[0] in List[i][k] and rule[1] in List[k + 1][j]:
                            List[i][j].add(head)

    return len(List[0][length - 1]) != 0