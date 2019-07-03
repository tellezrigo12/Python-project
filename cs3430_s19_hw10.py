#!/usr/bin/python3

import math
import Image


#######################################################
# module: cs3430_s19_hw10.py
# Rigoberto Tellez
# A02169682
########################################################

##################### Problem 1 (4 points) ####################

## a function to convert an rgb 3-tuple to a grayscale value.
def luminosity(rgb, rcoeff=0.2126, gcoeff=0.7152, bcoeff=0.0722):
    return rcoeff * rgb[0] + gcoeff * rgb[1] + bcoeff * rgb[2]


def save_gd_edges(input_fp, output_fp, magn_thresh=20):
    input_image = Image.open(input_fp)
    output_image = gd_detect_edges(input_image, magn_thresh=magn_thresh)
    output_image.save(output_fp)
    del input_image
    del output_image


def gd_detect_edges(rgb_img, magn_thresh=20):
    img = Image.open(rgb_img)
    finalImg = Image.new('L', (img.size[0], img.size[1]))
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            if col not in [0, (img.size[1]-1)] and row not in [0, (img.size[0] - 1)]:
                leftLumin = luminosity(img.getpixel(((row - 1), col)))
                rightLumin = luminosity(img.getpixel(((row+1), col)))
                topLumin = luminosity(img.getpixel((row, (col+1))))
                bottomLumin = luminosity(img.getpixel((row, (col-1))))
                dy = leftLumin - rightLumin
                dx = topLumin - bottomLumin
                gradMag = math.sqrt((dx)**2 + (dy)**2)
                if gradMag >= magn_thresh:
                    finalImg.putpixel((row, col), 255)
                else:
                    finalImg.putpixel((row, col), 0)
            else:
                finalImg.putpixel((row, col), 0)
    return finalImg
###################### Problem 2 (1 point) #####################

def cosine_sim(img1, img2):
    assert img1.size == img2.size
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for row in range(img1.size[0]):
        for col in range(img2.size[1]):
            numerator += (img1.getpixel((row, col)) * img2.getpixel((row,col)))
            denominator1 += (img1.getpixel((row, col)))**2
            denominator2 += (img2.getpixel((row,col)))**2
    finalDenom = math.sqrt(denominator1) * math.sqrt(denominator2)
    return numerator/finalDenom





def test_cosine_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = cosine_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)


def euclid_sim(img1, img2):
    assert img1.size == img2.size
    sqDif = 0
    for row in range(img1.size[0]):
        for col in range(img1.size[1]):
            sqDif+= (img1.getpixel((row,col)) - img2.getpixel((row,col)))**2
    return math.sqrt(sqDif)



def test_euclid_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = euclid_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)


def jaccard_sim(img1, img2):
    assert img1.size == img2.size
    S_1 = set()
    S_2 = set()
    for row in range(img1.size[0]):
        for col in range(img2.size[1]):
            S_1.add(img1.getpixel((row,col)))
            S_2.add(img2.getpixel((row, col)))
    return len(set.intersection(S_1, S_2))/len(set.union(S_1, S_2))





def test_jaccard_sim(img_fp1, img_fp2):
    img1 = Image.open(img_fp1)
    img2 = Image.open(img_fp2)
    sim = jaccard_sim(img1, img2)
    del img1
    del img2
    print(img_fp1, img_fp2)
    print(sim)


def test_01():
    save_gd_edges('img/1b_bee_01.png', 'img/1b_bee_01_ed.png', magn_thresh=20)
    save_gd_edges('img/1b_bee_10.png', 'img/1b_bee_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_10.png', 'img/2b_nb_10_ed.png', magn_thresh=20)
    save_gd_edges('img/2b_nb_21.png', 'img/2b_nb_21_ed.png', magn_thresh=20)
    save_gd_edges('img/elephant.jpg', 'img/elephant_ed.jpg', magn_thresh=20)
    save_gd_edges('img/output11885.jpg', 'img/output11885_ed.jpg', magn_thresh=20)
    save_gd_edges('img/2b_nb_09.png', 'img/2b_nb_09_ed.png', magn_thresh=20)
    save_gd_edges('img/output11884.jpg', 'img/output11884_ed.jpg', magn_thresh=20)


## testing the PIL/PILLOW installation
def test_02():
    img = Image.open('img/1b_bee_01.png').convert('LA')
    img2 = img.save('img/1b_bee_01_gray.png')
    del img
    del img2


if __name__ == '__main__':
    pass
