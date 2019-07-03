#!/usr/bin/python3

########################################
# module: cs3430_s19_hw11.py
# Rigoberto Tellez
# A02169682
########################################

## add your imports here
import math
import Image
import sys
import numpy as np
import cv2


from tof import tof
from const import const
from var import var
from pwr import pwr
from cs3430_s19_hw10 import gd_detect_edges
from deriv import deriv
from maker import make_const, make_pwr, make_prod, make_quot
from maker import make_plus, make_ln, make_absv
from maker import make_pwr_expr, make_e_expr
from plus import plus
from prod import prod





def nra(poly_fexpr, g, n):
   assert isinstance(g, const)
   assert isinstance(n, const)
   poly_fexprFunc = tof(poly_fexpr)
   poly_fexprPrime = deriv(poly_fexpr)
   poly_fexprPrimeF = tof(poly_fexprPrime)
   currGuessVal = g.get_val()
   for i in range(int(n.get_val())):
        prevVal = currGuessVal
        currGuessVal = prevVal  - (poly_fexprFunc(prevVal)/poly_fexprPrimeF(prevVal))
   return currGuessVal



def nra_ut_01():
    ''' Approximating x^2 - 2 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_02():
    ''' Approximating x^2 - 3 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-3.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_03():
    ''' Approximating x^2 - 5 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-5.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_04():
    ''' Approximating x^2 - 7 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-7.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_05():
    ''' Approximating e^-x = x^2. '''
    fexpr = make_e_expr(make_prod(make_const(-1.0),
                                  make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr,
                      make_prod(make_const(-1.0),
                                make_pwr('x', 2.0)))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_06():
    ''' Approximating 11^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-11.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_07():
    ''' Approximating 6^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-6.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_08():
    ''' Approximating x^3 + 2x + 2. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_prod(make_const(2.0),
                                make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr, make_const(2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_09():
    ''' Approximating x^3 + x - 1. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-1.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


def nra_ut_10():
    ''' Approximating e^(5-x) = 10 - x. '''
    fexpr = make_e_expr(make_plus(make_const(5.0),
                                  make_prod(make_const(-1.0),
                                            make_pwr('x', 1.0))))
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-10.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))
def nra_ut_11():
    #approximate sqrt(2.5)
    fexpr = make_plus(make_pwr('x', 2.0), const(-2.5))
    approx = nra(fexpr, const(1.0), const(1000000))
    assert abs(approx - math.sqrt(2.5)) <= .00001
    print('Good approxmiation')
def nra_ut_12():
    #approxmiate 9^{1/4}
    fexpr = make_plus(make_pwr('x', 4.0), const(-9.0))
    approx = nra(fexpr, const(1.0), const(1000000))
    assert abs(approx - 9**.25) <= .00001
    print('Good approxmiation')
def nra_ut_13():
    #approximate a zero for x^3-3x^2+14x-2
    f1 = make_plus(make_pwr('x', 3.0), make_prod(const(-3.0), make_pwr('x', 2.0)))
    f2 = make_plus(make_prod(const(14.0), make_pwr('x', 1.0)), const(-2.0))
    fexpr = make_plus(f1, f2)
    approx = nra(fexpr, const(1.0), const(1000000))
    print(approx)
def nra_ut_14():
    #approximate a zero for x^2 - 17x + 14
    f1 = make_plus(make_pwr('x', 2.0), make_prod(const(-17.0), make_pwr('x', 1.0)))
    fexpr = make_plus(f1, const(14.0))
    approx = nra(fexpr, const(1.0), const(1000000))
    gt = (17- math.sqrt(233))/2
    assert (approx - gt) <= .00001
    print('Good approximation')
def nra_ut_15():
    f1 = make_prod(const(60.0), make_quot(make_plus(const(1.0), make_prod(const(-1.0),make_pwr_expr(make_plus(const(1.0), make_pwr('x', 1.0)), const(-6)))), make_pwr('x', 1.0)))
    f2 = make_prod(const(995.0), make_pwr_expr(make_plus(const(1.0), make_pwr('x', 1.0)), const(-6.5)))
    fsum = make_plus(f1, f2)
    fexpr = make_plus(fsum, const(-970))
    approx = nra(fexpr, const(0.03), const(1000000))
    print(approx)
# =================== Problem 2 (4 points) ===================

def ht_detect_lines(img_fp, magn_thresh=20, spl=20):
    gd_img = gd_detect_edges(img_fp, magn_thresh)
    img = cv2.imread(img_fp)
    img_fp = Image.open(img_fp)
    width = img_fp.size[0]
    height = img_fp.size[1]
    diagonal = math.sqrt(width**2 + height**2)
    rhoThetaTable = []
    zeroRow =[]
    for i in range(int(diagonal) + 2):
        for j in range(0, 360):
            zeroRow.append(0)
        rhoThetaTable.append(zeroRow)
        zeroRow = []
    for row in range(int(gd_img.size[0])):
        for col in range(gd_img.size[1]):
            if gd_img.getpixel((row, col)) == 255:
                for theta in range(0, 360):
                    rho = int((row * math.cos(math.radians(theta)) + col*math.sin(math.radians(theta))))
                    rhoThetaTable[rho][theta] += 1
    for rho in range(int(diagonal) + 2):
        for theta in range(0, 360):
            if rhoThetaTable[rho][theta] > spl:
                a = math.cos(math.radians(theta))
                b = math.sin(math.radians(theta))
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return img_fp, img, gd_img, rhoThetaTable

def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff * rgb[0] + gcoeff * rgb[1] + bcoeff * rgb[2]
def getGrad(img, row, col, rMax, cMax):
    if col not in [0, (cMax-1)] and row not in [0, (rMax-1)]:
        leftLumin = luminosity(img.getpixel(((row - 1), col)))
        rightLumin = luminosity(img.getpixel(((row + 1), col)))
        topLumin = luminosity(img.getpixel((row, (col + 1))))
        bottomLumin = luminosity(img.getpixel((row, (col - 1))))
        dy = leftLumin - rightLumin
        dx = topLumin - bottomLumin
        gradMag = math.sqrt((dx) ** 2 + (dy) ** 2)
        return gradMag
    else:
        return 0



################ Unit Tests for Problem 2 ####################
##
## I used Image for edge detection and numpy image representation
## to draw lines. Hence, I am using cv2.imwrite to save the
## image with drawn line (lnimg) and image.save to save the image
## with the edges. Feel free to modify but keep the signatures
## of these tests the same.

def ht_test_01(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imshow('line detection', lnimg)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('im01_ln.png', lnimg)
    edimg.save('im01_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_02(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im02_ln.png', lnimg)
    edimg.save('im02_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_03(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im03_ln.png', lnimg)
    cv2.imshow('line detection', lnimg)
    cv2.waitKey()
    cv2.destroyAllWindows()
    edimg.save('im03_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_04(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im04_ln.png', lnimg)
   # edimg.save('im04_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_05(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im05_ln.png', lnimg)
    edimg.save('im05_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_06(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im06_ln.png', lnimg)
    edimg.save('im06_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_07(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im07_ln.png', lnimg)
    edimg.save('im07_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_08(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im08_ln.png', lnimg)
    edimg.save('im08_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_09(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im09_ln.png', lnimg)
    edimg.save('im09_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_10(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im10_ln.png', lnimg)
    edimg.save('im10_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_11(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im11_ln.png', lnimg)
    edimg.save('im11_ed.png')
    del img
    del lnimg
    del edimg


def ht_test_12(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im12_ln.png', lnimg)
    edimg.save('im12_ed.png')
    del img
    del lnimg
    del edimg


if __name__ == '__main__':
  nra_ut_15()