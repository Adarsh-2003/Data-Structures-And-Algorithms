with open("File Handling\poem.txt",'r') as f:
    f_out = open("File Handling\output.txt", 'w')
    for line in f:
        token = line.split(" ")
        wordCount = str(len(token))
        f_out.write(line + "WordCount : " + wordCount + " ")
    f_out.close()