a = []


def modern_print(s):
    if s not in a:
        print(s)
        a.append(s)
