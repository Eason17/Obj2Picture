import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('glass_down.png')
HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv_list = []
x_coordinate_list = []


def getpos(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(HSV[y, x])
        hsv_list.append(HSV[y, x].tolist())
        x_coordinate_list.append(x)


if __name__ == "__main__":
    cv2.imshow("imageHSV", HSV)
    cv2.imshow('image', image)
    cv2.setMouseCallback("imageHSV", getpos)
    cv2.waitKey(0)
    
    h_list = [item[0] for item in hsv_list]
    s_list = [item[1] for item in hsv_list]
    v_list = [item[2] for item in hsv_list]

    h_res = sorted(list(zip(x_coordinate_list, h_list)))
    s_res = sorted(list(zip(x_coordinate_list, s_list)))
    v_res = sorted(list(zip(x_coordinate_list, v_list)))

    plt.subplot(311)
    plt.plot([item[0] for item in h_res], [item[1] for item in h_res])
    plt.ylabel('H')
    plt.subplot(312)
    plt.plot([item[0] for item in s_res], [item[1] for item in s_res])
    plt.ylabel('S')
    plt.subplot(313)
    plt.plot([item[0] for item in v_res], [item[1] for item in v_res])
    plt.ylabel('V')
    plt.show()
