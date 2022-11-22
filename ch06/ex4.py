for a in range(2, 10, 1) :
    print("# %d단 #" % a)
    for b in range(1, 10, 1) :
        print("%d * %d = %d" %(a, b, (a * b)))

for a in range(2, 10, 1) :
    print("# %d단 #" %a)
    for b in range(2, 10, 1) :
        print("%d * %d = %d" %(b, a, (a * b)))