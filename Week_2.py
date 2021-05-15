with open("odev(1).txt","r") as first:
    new = first.read()
    for i in new:
        if i.isalpha() == False:
            new = new.replace(i,"")
        else:
            continue

print(new)