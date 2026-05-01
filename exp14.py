def check(sentence):
    words = sentence.lower().split()

    if len(words) < 2:
        return "Invalid sentence"

    subject = words[0]
    verb = words[1]

    # CFG-style categories
    singular_np = ["he", "she", "it", "ram"]
    plural_np = ["they", "we", "ram and shyam"]

    singular_vp = ["runs", "eats", "plays"]
    plural_vp = ["run", "eat", "play"]

    # Apply rules
    if subject in singular_np and verb in singular_vp:
        return "Correct (S → NP(singular) VP(singular))"
    elif subject in plural_np and verb in plural_vp:
        return "Correct (S → NP(plural) VP(plural))"
    else:
        return "Incorrect agreement"

s = input("Enter sentence: ")
print(check(s))