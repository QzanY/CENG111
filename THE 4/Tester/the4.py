def reader(a:str):
    a1 = a.split("=")
    func = a1[0].lstrip(" ")[0]
    a2 = a1[1].lstrip(" ").rstrip(" ")
    newa2 = ""
    for i in a2:
        if i != " ":
            newa2 += i
    for j in newa2:
        if j in "+-*^":
            op = j
            aa = newa2.split(j)
            if "(" in aa[0]:
                var1 = aa[0][0]
            else:
                var1 = aa[0]
            if "(" in aa[1]:
                var2 = aa[1][0]
            else:
                var2 = aa[1]
            break
    return([func,op,[var1],[var2]])
def construct_forest(defs:list):
    functions = "qwertyuıopğüasdfghjklşizcvbnmöç"
    nodes = [reader(d) for d in defs]
    def_dict = dict()
    for node in nodes:
        def_dict [node[0]] = node
    funcs = [node[0] for node in nodes]
    forest = []
    used = set()
    for node in def_dict:
        if def_dict[node][2][0] in functions:
            def_dict[node][2] = def_dict[def_dict[node][2][0]]
            used.add(def_dict[node][2][0])
        if def_dict[node][3][0] in functions:
            def_dict[node][3] = def_dict[def_dict[node][3][0]]
            used.add(def_dict[node][3][0])
    for func in def_dict:
        if func not in used:
            forest.append(def_dict[func])
    return(forest)
