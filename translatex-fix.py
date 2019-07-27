#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) < 2:
        print("Please pass your filename as an argument")
        return 1

    in_file = open(sys.argv[1],'r')

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

    return 0

if __name__ == "__main__":
    main()
