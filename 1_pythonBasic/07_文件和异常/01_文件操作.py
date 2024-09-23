with open("a.txt", "r", encoding="utf-8") as f:
    for i in f:
        print(i, end='')

    f.close()

with open("a.txt", "r", encoding="utf-8") as f:
    result = f.read()
    print(result)
    f.close()

with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hello world")
    f.close()

with open("a.txt", "r", encoding="utf-8") as f:
    result1 = f.read()
    print(result1)
    f.close()
