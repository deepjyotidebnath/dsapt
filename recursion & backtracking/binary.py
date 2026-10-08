def generate(n, s=""):
    if len(s)==n:
        print(s)
        return
    generate(n, s+"0")
    generate(n, s+"1")
generate(3)
        