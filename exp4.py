def plural_fsm(word):
    state = 0

    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        state = 1
    elif word.endswith('y') and word[-2] not in 'aeiou':
        state = 2
    else:
        state = 3

    if state == 1:
        return word + "es"
    elif state == 2:
        return word[:-1] + "ies"
    elif state == 3:
        return word + "s"


words = ["cat", "bus", "box", "baby", "brush"]

for w in words:
    print(w, "->", plural_fsm(w))