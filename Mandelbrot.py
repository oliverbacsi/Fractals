#!/usr/bin/env python3

######################################
# Mandelbrot generator in ANSI
#
import os,sys,re
from math import log
from _palette import PALETTE
from PIL import Image
import time

# Screen max sizes
XSIZE   :int  = int(os.environ["COLUMNS"])
YSIZE   :int  = int(os.environ["LINES"])-1
# Max number of iterations before stop and evaluate if divergent or not
MAXITER :int  = 500
# Complex vector length treshold to consider iteration as divergent
MaxVect :float = 3.0
# Whether display should be color or mono.
CLR     :str  = "CLR"
# Image palette pre-calculated list for screen shots.
IPALR   :list = [255]
IPALG   :list = [255]
IPALB   :list = [255]


# Command line arguments :
# Mxxx  = Max Iterations (xxx is integer)
# Vx.yy = Max Vector Length to state it is divergent (x.yy is float)
# B     = Switch to B&W Palette
for parm in sys.argv[1:] :
    m = re.match("([BMV])([0-9\.\-\+e]*)",parm,re.I)
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
        elif m[1].upper() == "B" :
            CLR = "B_W"

# Initial value ranges to display (position and zoom)
Scr_X_L :float = -2.50
Scr_X_R :float = +1.00
Scr_Y_T :float = +1.12
Scr_Y_B :float = -1.12
# Rate between iteration numbers and palette index to display
PalRate :float = 1.0 * (len(PALETTE[CLR])-1) / log(MAXITER)


###

def clamp(_val :float, _max :float, _min :float) -> float :
    if _val > _max : _val = _max
    if _val < _min : _val = _min
    return _val


def exportImage(IWid :int, IHei :int) -> None :
    """Export a detailed image file from the current view.
    Parameters:
    :param IWid : Image Width in Pixels. (ex: 1920)
    :param IHei : Image Height in Pixels. (ex: 1080)
    :returns : None"""
    global Scr_X_R, Scr_X_L, Scr_Y_T, Scr_Y_B, MaxVect, MAXITER
    global IPALR, IPALG, IPALB

    Img = Image.new("RGB",(IWid,IHei))
    IL = list(())
    for j in range(IHei) :
        print(str(j))
        for i in range(IWid) :
            Re0 = (Scr_X_R - Scr_X_L) * i / (IWid-1) + Scr_X_L
            Im0 = (Scr_Y_B - Scr_Y_T) * j / (IHei-1) + Scr_Y_T
            Re = 0.0
            Im = 0.0
            Iter = 0
            while Re*Re + Im*Im <= MaxVect*MaxVect and Iter < MAXITER :
                Re_tmp = Re*Re - Im*Im + Re0
                Im = 2*Re*Im + Im0
                Re = Re_tmp
                Iter += 1
            IL.append( tuple((IPALR[Iter],IPALG[Iter],IPALB[Iter])) )
    Img.putdata(IL)
    Img.save("Screenshots/Mand-"+str(time.time_ns())+".png")

###

# Generate the large pallet for the image exporting so that we don't have to regenerate each time
for i in range(1,MAXITER+1) :
    rt = log(1000*i/MAXITER)

    if rt < 3 :
        IPALR.append(0)
    elif rt > 4 :
        IPALR.append(255)
    else :
        IPALR.append(clamp(int(255*(rt-3)),255,0))

    if rt < 1 :
        IPALG.append(0)
    elif rt < 2 :
        IPALG.append(clamp(int(255*(rt-1)),255,0))
    elif rt < 4 :
        IPALG.append(255)
    elif rt < 5 :
        IPALG.append(clamp(int(255*(5-rt)),255,0))
    elif rt < 6 :
        IPALG.append(0)
    else :
        IPALG.append(clamp(int(255*(rt-6)),255,0))

    if rt < 1 :
        IPALB.append(clamp(int(255*rt),255,0))
    elif rt < 2 :
        IPALB.append(255)
    elif rt < 3 :
        IPALB.append(clamp(int(255*(3-rt)),255,0))
    elif rt < 5 :
        IPALB.append(0)
    elif rt < 6 :
        IPALB.append(clamp(int(255*(rt-5)),255,0))
    else :
        IPALB.append(255)

IPALR[-1] = 0
IPALG[-1] = 0
IPALB[-1] = 0


while True :
    print("\x1b[0m\x1b[2J\x1b[H",end="")
    for SY in range(YSIZE) :
        for SX in range(XSIZE) :
            Re0 = (Scr_X_R - Scr_X_L) * SX / (XSIZE-1) + Scr_X_L
            Im0 = (Scr_Y_B - Scr_Y_T) * SY / (YSIZE-1) + Scr_Y_T
            Re = 0.0
            Im = 0.0
            Iter = 1   # To avoid log(0), and the actual value doesn't really matter
            while Re*Re + Im*Im <= MaxVect*MaxVect and Iter < MAXITER :
                Re_tmp = Re*Re - Im*Im + Re0
                Im = 2*Re*Im + Im0
                Re = Re_tmp
                Iter += 1
            print(PALETTE[CLR][int(log(Iter)*PalRate)],end="")
    print(f"\x1b[1;36;44m Rmax = {MaxVect} \x1b[0m   \x1b[1;35;45m ITmax = {MAXITER} \x1b[0m   \x1b[1;33;42m Re: {Scr_X_L} .. {Scr_X_R} \x1b[0m   \x1b[1;31;43m Im: {Scr_Y_B} .. {Scr_Y_T} ",end="\x1b[0m")
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
    elif Ans.upper() == "I" :
        exportImage(3840,2160)
    elif Ans.upper() == "Q" :
        break
