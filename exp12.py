def earley(grammar, string):
    n = len(string)
    chart = [set() for _ in range(n + 1)]
    chart[0].add(("S'", ["S"], 0, 0))

    for i in range(n + 1):
        for state in list(chart[i]):
            lhs, rhs, dot, start = state

            if dot < len(rhs):
                symbol = rhs[dot]

                if symbol in grammar:
                    for prod in grammar[symbol]:
                        chart[i].add((symbol, prod, 0, i))

                elif i < n and symbol == string[i]:
                    chart[i + 1].add((lhs, rhs, dot + 1, start))

            else:
                for st in chart[start]:
                    st_lhs, st_rhs, st_dot, st_start = st
                    if st_dot < len(st_rhs) and st_rhs[st_dot] == lhs:
                        chart[i].add((st_lhs, st_rhs, st_dot + 1, st_start))

    return ("S'", ["S"], 1, 0) in chart[n]

grammar = {
    "S": [["a", "S", "b"], []]
}
string = input("Enter string: ")

if earley(grammar, string):
    print("Accepted")
else:
    print("Rejected")