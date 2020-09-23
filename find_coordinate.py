import ADBShell
import cv2
import AshenArms
import numpy as np
from config import SCREEN_SHOOT_SAVE_PATH

def match_tpl_loc(target, tpl):
    img_target = cv2.imread(target)
    img_tpl = cv2.imread(tpl)
    methods = [cv2.TM_CCOEFF_NORMED]
    th, tw = img_tpl.shape[:2]
    for md in methods:
        result = cv2.matchTemplate(img_target, img_tpl, md)
        loc = result[np.where(result >= 0.9)]
        print(loc)
    return loc


if __name__ == '__main__':
    a = ADBShell.ADBShell()
    a.get_screen_shoot()
    ADBShell.ADBShell.get_sub_screen("1.png", AshenArms.box, "temp.png")
    # match_tpl_loc(a.SCREEN_SHOOT_SAVE_PATH+"1.png", a.SCREEN_SHOOT_SAVE_PATH+"3star.png")
    target = cv2.imread("{}".format(a.SCREEN_SHOOT_SAVE_PATH+"1.png"))
    tpl = cv2.imread("{}".format(a.SCREEN_SHOOT_SAVE_PATH + "3star.png"))

    methods = [cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        result = cv2.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if md == cv2.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        print(tl)

