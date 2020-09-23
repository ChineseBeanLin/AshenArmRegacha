import ADBShell
import cv2
import numpy as np
from config import SCREEN_SHOOT_SAVE_PATH

prefix_x = 745-560
y = [290, 510]
box = [[190, 290],
       [126, 29]]
skip_box = [[1117, 26], [115, 42]]
random_click = [[50, 50], [1000, 100]]
redraw_box = [[410, 629], [200, 62]]
redraw_confirm_box = [[660, 414], [198, 72]]


def match_tpl_loc(target, tpl):
    img_target = cv2.imread(target)
    img_tpl = cv2.imread(tpl)
    methods = [cv2.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        result = cv2.matchTemplate(img_target, img_tpl, md)
        loc = np.where(result >= 0.9)
        print(loc)
        return loc


def count_3star_num():
    num = 0
    for i in range(0, 2):
        box[0][0] = 190
        box[0][1] = y[i]
        for j in range(0, 5):
            ADBShell.ADBShell.get_sub_screen(screen_shot_name, box, "temp.png")
            screenshot = SCREEN_SHOOT_SAVE_PATH + "temp.png"
            template = SCREEN_SHOOT_SAVE_PATH + "3star.png"
            if ADBShell.ADBShell.image_compare(screenshot, template):
                num += 1
            box[0][0] += prefix_x
    return num


def redraw(adb_shell):
    adb_shell.get_mouse_click_random(redraw_box)
    adb_shell.wait(0, 1)
    adb_shell.get_mouse_click_random(redraw_confirm_box)
    adb_shell.wait(4, 1)
    adb_shell.get_screen_shoot(screen_range=skip_box)
    while not (ADBShell.ADBShell.image_compare(SCREEN_SHOOT_SAVE_PATH + "skip.png",
                                               SCREEN_SHOOT_SAVE_PATH + "1.png")):
        adb_shell.get_mouse_click_random(random_click)
        adb_shell.wait(1, 1)
        adb_shell.get_screen_shoot(screen_range=skip_box)


if __name__ == '__main__':
    screen_shot_name = "1.png"
    a = ADBShell.ADBShell()
    t = 0
    num_3star = 0
    while num_3star < 2:
        redraw(a)
        a.get_mouse_click_random(skip_box)
        a.wait(2, 1)
        a.get_screen_shoot()
        num_3star = count_3star_num()
        t += 1
        print("第" + str(t) + "次：" + str(num_3star) + "个三星")
