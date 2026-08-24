expression = input("Enter expression (Example: Human(Socrates)): ")

if "(" in expression and ")" in expression:
    predicate = expression.split("(")[0]
    argument = expression.split("(")[1].replace(")", "")

    print("Predicate:", predicate)
    print("Argument:", argument)
else:
    print("Invalid Expression")