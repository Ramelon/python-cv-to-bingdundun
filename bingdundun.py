import turtle as t
import cv2 # pip install opencv-python

t.getscreen().colormode(255)
# 这里的图片用自己的路径替换即可
img1 = cv2.imread(r'C:\Users\VULCAN\Desktop\bingdundun.png')[0: -2: 2]
width = len(img1[0])
height = len(img1)
t.setup(width=width / 2 + 300, height=height + 300)
t.pu()
t.goto(-width / 4 + 10, height / 2 - 10)
t.pd()
t.tracer(2000)
for k1, i in enumerate(img1):
    for j in i[::2]:
        t.pencolor((j[0], j[1], j[2]))
        t.fd(1)
    t.pu()
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)
    t.pd()
t.done()
