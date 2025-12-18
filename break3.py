details = [{'a':3, 'b':5, 'c':7},{'d':9, 'e':11},{'f':13}]
a = str(len(list(details[0].items()))) + str(len(list(details[1].items()))) + str(len(list(details[2].items())))
for i in a:
    print(i * 3)
    if i == 3:
        continue
 