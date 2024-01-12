#!/usr/bin/env python3

######################################
# Mandelbrot generator in ANSI
#
import os,sys,re
from math import log

#PALETTE :list = [15, 231, 225, 219, 213, 207, 201, 200, 199, 198, 197, 196, 202, 208, 214, 220, 226, 190, 184, 148, 142, 106, 70, 64, 28, 34, 40, 46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21, 20, 19, 18, 17, 236]

PALETTE :list = [17, 18, 19, 20, 21, 27, 33, 39, 45, 51, 50, 49, 48, 47, 46, 40, 34, 28, 64, 70, 106, 142, 148, 184, 190, 226, 220, 214, 208, 202, 196, 197, 198, 199, 200, 201, 207, 213, 219, 225, 231, 15, 236]


XSIZE   :int  = int(os.environ["COLUMNS"])
YSIZE   :int  = int(os.environ["LINES"])-1
MAXITER :int  = 500
MaxVect :float = 3.0
InitRe  :float = 0.11
InitIm  :float = 0.62

# Command line arguments :
# Mxxx  = Max Iterations (xxx is integer)
# Vx.yy = Max Vector Length to state it is divergent (x.yy is float)
# Rx.yy = Real component of initial complex value (x.yy is float)
# Ix.yy = Imag component of initial cimplex value (x.yy is float)
for parm in sys.argv[1:] :
    m = re.match("([MVRI])([0-9\.\-\+e]+)",parm,re.I)
    if m :
        if m[1].upper() == "M" :
            try :
                reqIter = int(m[2])
            except ValueError :
                pass
            else :
                if reqIter > 5 : MAXITER = reqIter
        elif m[1].upper() == "V" :
            try :
                reqRad = float(m[2])
            except ValueError :
                pass
            else :
                if reqRad > 0.0 : MaxVect = reqRad
        elif m[1].upper() == "R" :
            try :
                reqReal = float(m[2])
            except ValueError :
                pass
            else :
                InitRe = reqReal
        elif m[1].upper() == "I" :
            try :
                reqImag = float(m[2])
            except ValueError :
                pass
            else :
                InitIm = reqImag

Scr_X_L :float = (-0.7) * MaxVect
Scr_X_R :float = 0.7 * MaxVect
Scr_Y_T :float = 0.4 * MaxVect
Scr_Y_B :float = (-0.4) * MaxVect
PalRate :float = 42.0 / log(MAXITER)

while True :
    print("\x1b[0m\x1b[2J\x1b[H",end="")
    for SY in range(YSIZE) :
        for SX in range(XSIZE) :
            Re = (Scr_X_R - Scr_X_L) * SX / (XSIZE-1) + Scr_X_L
            Im = (Scr_Y_B - Scr_Y_T) * SY / (YSIZE-1) + Scr_Y_T
            Iter = 0
            while Re*Re + Im*Im <= MaxVect*MaxVect and Iter < MAXITER :
                Re_tmp = Re*Re - Im*Im + InitRe
                Im = 2*Re*Im + InitIm
                Re = Re_tmp
                Iter += 1
            print("\x1b[38;5;"+str(PALETTE[int(log(Iter)*PalRate)])+"m▓",end="")
    print(f"\x1b[1;37;41m C=[{InitRe}+i{InitIm}] \x1b[0m   \x1b[1;36;44m Rmax = {MaxVect} \x1b[0m   \x1b[1;35;45m ITmax = {MAXITER} \x1b[0m   \x1b[1;33;42m Re: {Scr_X_L} .. {Scr_X_R} \x1b[0m   \x1b[1;31;43m Im: {Scr_Y_B} .. {Scr_Y_T} ",end="\x1b[0m")
    Ans = input(" >>> ")
    Wid = Scr_X_R-Scr_X_L
    Hei = Scr_Y_T-Scr_Y_B
    if Ans.upper() == "U" :
        Scr_Y_T = Scr_Y_T + Hei/5.0
        Scr_Y_B = Scr_Y_B + Hei/5.0
    elif Ans.upper() == "D" :
        Scr_Y_T = Scr_Y_T - Hei/5.0
        Scr_Y_B = Scr_Y_B - Hei/5.0
    elif Ans.upper() == "L" :
        Scr_X_L = Scr_X_L - Wid/5.0
        Scr_X_R = Scr_X_R - Wid/5.0
    elif Ans.upper() == "R" :
        Scr_X_L = Scr_X_L + Wid/5.0
        Scr_X_R = Scr_X_R + Wid/5.0
    elif Ans.upper() == "+" :
        Scr_X_L = Scr_X_L + Wid/4.0
        Scr_X_R = Scr_X_R - Wid/4.0
        Scr_Y_T = Scr_Y_T - Hei/4.0
        Scr_Y_B = Scr_Y_B + Hei/4.0
    elif Ans.upper() == "-" :
        Scr_X_L = Scr_X_L - Wid/2.0
        Scr_X_R = Scr_X_R + Wid/2.0
        Scr_Y_T = Scr_Y_T + Hei/2.0
        Scr_Y_B = Scr_Y_B - Hei/2.0
    elif Ans.upper() == "Q" :
        break
