def binary(n, path):
    if len(path)==n:
        print(path)
        return
    binary(n, path + "0")
    binary(n, path + "1")

binary(3,"")