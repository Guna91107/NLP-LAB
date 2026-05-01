def pcfg(sentence):
    words = sentence.lower().split()

    if len(words) != 2:
        return "Invalid sentence"

    prob = 1.0

    if words[0] == "he":
        prob *= 0.5
    elif words[0] == "she":
        prob *= 0.5
    else:
        return "Not in grammar"

    if words[1] == "runs":
        prob *= 0.6
    elif words[1] == "eats":
        prob *= 0.4
    else:
        return "Not in grammar"

    return prob

s = input("Enter sentence: ")
result = pcfg(s)

if isinstance(result, float):
    print("Valid sentence")
    print("Probability =", result)
else:
    print(result)