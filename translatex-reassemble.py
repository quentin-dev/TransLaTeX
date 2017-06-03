out_file = open("out.txt",'w')

for x in range(0,7):
    inbal_file = open(str(x)+"-bal.txt",'r')
    intxt_file = open(str(x)+"-en.txt",'r')
    for line in inbal_file:
        if line[0] == "l":
            out_file.write(intxt_file.readline())
        else:
            out_file.write(line)
