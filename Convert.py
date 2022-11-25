from Processing import isTerminal, isVariables

def CFGtoCNF(CFG):
    headList = list(CFG.keys())
    bodyList = list(CFG.values())
    SS = headList[0]
    addRule = False

    for rules in bodyList:
        for rule in rules:
            if SS in rule:
                addRule = True
                break
        if addRule:
            break

    if addRule:
        newRule = {"START" : [[SS]]}
        newRule.update(CFG)
        CFG = newRule

    containUnit = True

    while containUnit:
        unitProd = {}
        containUnit = False
        
        for head, body in CFG.items():
            for rule in body:
                if len(rule) == 1 and isVariables(rule[0]):
                    containUnit = True
                    if head not in unitProd.keys():
                        unitProd[head] = [[rule[0]]]
                    else:
                        unitProd[head].append([rule[0]])

        for headUnit, bodyUnit in unitProd.items():
            for ruleUnit in bodyUnit:
                for head, body in CFG.items():
                    if len(ruleUnit) == 1 and head == ruleUnit[0]:
                        newRule = {headUnit : body}
                        if headUnit not in CFG.keys():
                            CFG[headUnit] = body
                        else:
                            for rule in body:
                                if rule not in CFG[headUnit]:
                                    CFG[headUnit].append(rule)
    
        for headUnit, bodyUnit in unitProd.items():
            for ruleUnit in bodyUnit:
                if len(ruleUnit) == 1:
                    CFG[headUnit].remove(ruleUnit)

    newProd = {}
    deleteProd = {}

    i = 0
    for head, body in CFG.items():
        for rule in body:
            headSymbol = head
            temp = [r for r in rule]
            if len(temp) > 2:
                while len(temp) > 2:
                    newSymbol = f"X{i}"
                    if headSymbol not in newProd.keys():
                        newProd[headSymbol] = [[temp[0], newSymbol]]
                    else:
                        newProd[headSymbol].append([temp[0], newSymbol])
                    headSymbol = newSymbol
                    temp.remove(temp[0])
                    i += 1
                else:
                    if headSymbol not in newProd.keys():
                        newProd[headSymbol] = [temp]
                    else:
                        newProd[headSymbol].append(temp)
                    
                    if head not in deleteProd.keys():
                        deleteProd[head] = [rule]
                    else:
                        deleteProd[head].append(rule)

    for newHead, newBody in newProd.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else:
            CFG[newHead].extend(newBody)

    for deleteHead, deleteBody in deleteProd.items():
        for deleteRule in deleteBody:
            CFG[deleteHead].remove(deleteRule)

    newProd = {}
    deleteProd = {}

    j = 0
    k = 0
    for head, body in CFG.items():
        for rule in body:
            if len(rule) == 2 and isTerminal(rule[0]) and isTerminal(rule[1]):
                Y = f"Y{j}"
                Z = f"Z{k}"

                if head not in newProd.keys():
                    newProd[head] = [[Y, Z]]
                else:
                    newProd[head].append([Y, Z])
                    
                newProd[Y] = [[rule[0]]]
                newProd[Z] = [[rule[1]]]

                if head not in deleteProd.keys():
                    deleteProd[head] = [rule]
                else:
                    deleteProd[head].append(rule)

                j += 1
                k += 1

            elif len(rule) == 2 and isTerminal(rule[0]):
                Y = f"Y{j}"

                if head not in newProd.keys():
                    newProd[head] = [[Y, rule[1]]]
                else:
                    newProd[head].append([Y, rule[1]])

                newProd[Y] = [[rule[0]]]

                if head not in deleteProd.keys():
                    deleteProd[head] = [rule]
                else:
                    deleteProd[head].append(rule)

                j += 1

            elif len(rule) == 2 and isTerminal(rule[1]):
                Z = f"Z{k}"

                if head not in newProd.keys():
                    newProd[head] = [[rule[0], Z]]
                else:
                    newProd[head].append([rule[0], Z])

                newProd[Z] = [[rule[1]]]

                if head not in deleteProd.keys():
                    deleteProd[head] = [rule]
                else:
                    deleteProd[head].append(rule)

                k += 1

            else:
                pass

    for newHead, newBody in newProd.items():
        if newHead not in CFG.keys():
            CFG[newHead] = newBody
        else:
            CFG[newHead].extend(newBody)

    for deleteHead, deleteBody in deleteProd.items():
        for deleteRule in deleteBody:
            CFG[deleteHead].remove(deleteRule)

    return CFG