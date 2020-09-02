#ecoding=utf-8
# author:herui
# time:2020/8/24 15:08
# function:
import logging
import os
import time
import cv2
import numpy as np

class Utils(object):

    def get_pwd_pos(self, im, pwd):
        numbers = set(list(pwd))
        print(numbers)
        templates = {}
        positions = {}
        nimgpath = "./image/"  # 数字图片不在同目录时使用
        for i in numbers:
            templates[i] = os.path.join(nimgpath, "n{}.png".format(i))

        start = time.time()
        # 读源图片
        img_rgb = cv2.imread(im)
        print("原图尺寸：", img_rgb.shape)
        for teNum, tepath in templates.items():
            print("teNum: ", teNum)
            # print("tepath: ", tepath)
            # 读取模板图片
            template = cv2.imread(tepath)
            # print('图片尺寸:', template.shape)
            res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
            # 匹配度参数，1为完全匹配
            threshold = .80
            # 匹配程度大于%80的坐标y,x
            loc = np.where(res >= threshold)
            if len(loc) > 0:
                positions[teNum] = list(zip(*loc[::-1]))[0]
                # print("positions[%d]:--"%teNum,positions[teNum])
            else:
                print("Can not found number: [{}] in image: [{}].".format(tepath, im))

        end = time.time()
        print(end - start)
        return [positions[n] for n in pwd]

    @classmethod
    def screen_path(self,name=""):
        time_line = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.getcwd() + "\\" + "screen" + "\\"
        print(log_path)
        file_name = log_path + time_line + name +'.png'
        return file_name

