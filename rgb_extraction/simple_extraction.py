import cv2

img = cv2.imread('logo_red_hat_gray.png')

# Set blue and green channels to 0
b= img[:,:,0].copy()
img[:,:,0] = 0

g= img[:,:,1].copy()
img[:,:,1] = 0

cv2.imshow('single_channel_img', img)
cv2.waitKey()

img[:,:,0] = b #rimetto il blue
img[:,:,2] = 0 #tolgo il rosso

cv2.imshow('single_channel_img', img)
cv2.waitKey()

img[:,:,1] = g #rimetto il verde
img[:,:,0] = 0 #tolgo il blue

cv2.imshow('single_channel_img', img)
cv2.waitKey()
