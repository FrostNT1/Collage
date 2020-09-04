# Instagram Collage

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

# Importing the Images

bg = np.zeros([430,430,3], dtype = "uint8")
plt.imshow(bg)
plt.axis("Off")
plt.show()


"""
imgs = ["top_left.jpg","top_right.jpg","bottom_left.jpg","bottom_right.jpg"]
a,b,c,d = 10,210,10,210
for i in imgs:
    if i == "top_right.jpg":
        a,b,c,d = 10, 210, 220, 420, 
    elif i == "bottom_left.jpg":
        a,b,c,d = 220, 420, 10, 210
    elif i == "bottom_right.jpg":
        a,b,c,d = 220, 420, 220, 420
    inx = imgs.index(i)
    elem = cv2.imread(i)
    elem = cv2.cvtColor(elem, cv2.COLOR_BGR2RGB)
    elem = cv2.resize(elem, (200, 200))
    plt.imshow(elem)
    plt.axis("Off")
    plt.show()
    bg[a:b, c:d , :] = elem
    plt.imshow(bg)
    plt.axis("Off")
    plt.show()
"""


"""
for layer in range(3):
    for row in range(200):
        for column in range(200):
            bg[row + 10][column + 10][layer] = top_left[row][column][layer]
"""

plt.imshow(bg)
plt.axis("Off")
plt.show()

top_right = cv2.imread("top_right.jpg")
top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB)
top_right = cv2.resize(top_right, (200, 200))
plt.imshow(top_right)
plt.axis("Off")
plt.show()

bg[10:210, 220:420, :] = top_right
plt.imshow(bg)
plt.axis("Off")
plt.show()

bottom_left = cv2.imread("bottom_left.jpg")
bottom_left = cv2.cvtColor(bottom_left,cv2.COLOR_BGR2RGB)
bottom_left = cv2.resize(bottom_left, (200,200))
plt.imshow(bottom_left)
plt.axis(False)
plt.show()

bg[220:420, 10:210, :] = bottom_left
plt.imshow(bg)
plt.axis("Off")
plt.show()

bottom_right = cv2.imread("bottom_right.jpg")
bottom_right = cv2.cvtColor(bottom_right,cv2.COLOR_BGR2RGB)
bottom_right = cv2.resize(bottom_right, (200,200))
plt.imshow(bottom_right)
plt.axis(False)
plt.show()

bg[220:420, 220:420, :] = bottom_right
plt.imshow(bg)
plt.axis("Off")
plt.show()

border = np.zeros([120,120,3], dtype = "uint8")
center = cv2.imread("center.jpeg")
center = cv2.cvtColor(center, cv2.COLOR_BGR2RGB)
center = cv2.resize(center, (100, 100))
plt.imshow(center)
plt.axis(False)
plt.show()

border[10:110, 10:110, :] = center
plt.imshow(border)
plt.axis(False)
plt.show()

bg[155:275, 155:275, :] = border
plt.imshow(bg)
plt.axis("Off")
plt.show()

bg = cv2.cvtColor(bg,cv2.COLOR_RGB2BGR)
cv2.imwrite("Collage.jpg", bg)

bg = bg.reshape((430*430, 3))
df2 = pd.DataFrame(bg, dtype = 'uint16', columns = ['r', 'g', 'b'])
df2.to_csv('Image.csv', index = False)