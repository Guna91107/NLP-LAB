s = input("Enter sentence: ")

if "?" in s:
    print("Question")
elif s.lower().startswith(("go", "do", "make", "take")):
    print("Command")
else:
    print("Statement")