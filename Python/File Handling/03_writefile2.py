with open("File Handling\stocks.csv", 'r') as f, open("File Handling\stocks_out.csv", 'w') as fw:
    fw.write("Company Name, PER, PBS\n")
    next(f)
    for line in f:
        token = line.split(",")
        name = token[0]
        price = float(token[1])
        eps = float(token[2])
        book = float(token[3])
        per = round(price / eps,2)
        pbr = round(price / book,2)
        fw.write(f"{name} {per} {pbr}\n")
