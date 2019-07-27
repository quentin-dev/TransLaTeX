#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) < 2:
        print("Please pass the max number as an argument")
        return 1

    out_file = open("out.txt",'w')

    for x in range(0,int(sys.argv[1])):
        inbal_file = open(str(x)+"-bal.txt",'r')
        intxt_file = open(str(x)+"-en.txt",'r')
        for line in inbal_file:
            if line[0] == "l":
                out_file.write(intxt_file.readline())
            else:
                out_file.write(line)
    return 0

if __name__ == "__main__":
    main()
