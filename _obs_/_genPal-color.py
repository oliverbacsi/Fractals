#!/usr/bin/env python3

#pal :list = [15, 231, 225, 219, 213, 207, 201, 200, 199, 198, 197, 196, 202, 208, 214, 220, 226, 190, 184, 148, 142, 106, 70, 64, 28, 34, 40, 46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21, 20, 19, 18, 17, 236]
pal :list = [16, 17, 18, 19, 20, 21, 27, 33, 39, 45, 51, 50, 49, 48, 47, 46, 40, 34, 28, 64, 70, 106, 142, 148, 184, 190, 226, 220, 214, 208, 202, 196, 197, 198, 199, 200, 201, 207, 213, 219, 225, 231, 15, 16]

fout = open("_palette.py","w")
fout.write("PALETTE :list = [")

for i in range(len(pal)-1) :
    for j in [' ', '░', '▒', '▓'] :
        fout.write(f"\"\\x1b[48;5;{pal[i]}m\\x1b[38;5;{pal[i+1]}m{j}\", ")

fout.write(f"\"\\x1b[48;5;{pal[-1]}m\\x1b[38;5;{pal[-1]}m \"")
fout.write(f", \"\\x1b[48;5;{pal[-1]}m\\x1b[38;5;{pal[-1]}m \"")
fout.write("]\n\n")
fout.close()
