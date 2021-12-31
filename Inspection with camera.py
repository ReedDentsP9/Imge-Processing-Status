import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

vid=cv2.VideoCapture(0)
while (True):
    ret,frame=vid.read()
    frame1 = cv2.resize(frame, (1280, 720))
    
    grayscale=cv2.cvtColor(frame1 ,cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(grayscale, (15, 15), 1)
    edge_img = cv2.Canny(blur_image,100,200)

    try:
        contours, heirarchy = cv2.findContours(edge_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt = contours[0]
        area=cv2.contourArea(cnt)
    except:
        print("No Dent Found")
    
    area = cv2.contourArea(cnt)
    #print('Area of Dent=',area)

    cnt1=cv2.fillPoly(grayscale,pts=[cnt],color=(255,255,255))
    #print(cnt1.shape)
    
    pixelCount = []
    for i in range(cnt1.shape[0]):
        count = 0
        for j in range(cnt1.shape[1]):
            if cnt1[i][j] != 255:
                cnt1[i][j] = 0
            else:
                count += 1
        pixelCount.append(count)

    print(len(pixelCount))

    cv2.imshow("Cropped Image",cnt1)
    pixelCount=np.asarray(pixelCount)
    plt.plot(pixelCount)
    print (pixelCount.shape)   
    cv2.waitKey(1)

