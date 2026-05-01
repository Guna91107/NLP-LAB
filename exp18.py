def parse_fopc(expr):
    if "(" in expr and ")" in expr:
        predicate = expr.split("(")[0]
        args = expr.split("(")[1].replace(")", "").split(",")
        print("Predicate:", predicate)
        print("Arguments:", args)
    else:
        print("Invalid expression")

expr = input("Enter expression: ")
parse_fopc(expr)