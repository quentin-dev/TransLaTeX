in_file = open('input.txt','r')

linenum = 1

outtext_file = open("0-txt.txt", 'w')
outbal_file = open("0-bal.txt", "w")
for line in in_file:
    if linenum%100 == 0:
        outtext_file = open(str(linenum // 100)+"-txt.txt",'w')
        outbal_file = open(str(linenum // 100)+"-bal.txt",'w')
    if line[0] == "\\":
        outbal_file.write(line)
    else:
        outbal_file.write("line" + str(linenum)+"\n")
        outtext_file.write(line)
    linenum += 1