from sys import argv

with open("baker.csv", "a", encoding="utf-8") as sale_a:
    with open("baker.csv", "r", encoding="utf-8") as sale_r:
        if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").replace(",", "").isdigit()]:
            if len(argv) == 3:
                print(*sale_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep="\n")
            if "," in argv[1] or "." in argv[1]:
                sale_r.read()
                print(argv[1], file=sale_a)
            else:
                print(*sale_r.readlines()[int(argv[1]) - 1:])
        else:
            print(sale_r.read())
