def address(nw_address, n):
    a = format(format(n, "b"), "0>16")
    a1 = a[:8]
    a2 = a[8:]
    a1 = str(int(a1, 2))
    a2 = str(int(a2, 2))
    print(nw_address + a1 + "." + a2)
