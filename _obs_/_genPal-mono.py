#!/usr/bin/env python3

pal :list = [16]
for i in range(232,256) : pal.append(i)
pal.append(16)

fout = open("_palette.py","w")
fout.write("PALETTE :list = [")

for i in range(len(pal)-1) :
    for j in [' ', '░', '▒', '▓'] :
        fout.write(f"\"\\x1b[48;5;{pal[i]}m\\x1b[38;5;{pal[i+1]}m{j}\", ")

fout.write(f"\"\\x1b[48;5;{pal[-1]}m\\x1b[38;5;{pal[-1]}m \"")
fout.write(f", \"\\x1b[48;5;{pal[-1]}m\\x1b[38;5;{pal[-1]}m \"")
fout.write("]\n\n")
fout.close()

