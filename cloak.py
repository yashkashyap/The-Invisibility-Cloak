# USE A BLUE SHEET OF CLOTH AS THE INVISIBILITY CLOAK.

import numpy as np
import cv2

def main():

	cap = cv2.VideoCapture(0)

	bg = 0

	for i in range(50):
	    _, bg = cap.read()
	    
	while(1):
	    
	    _, frame = cap.read()
	    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	    lower = np.array([100, 50, 50])
	    upper = np.array([130, 255, 255])
	    
	    mask = cv2.inRange(hsv_image, lower, upper)
	    mask = cv2.medianBlur(mask, 9)
	    
	    mask_inv = cv2.bitwise_not(mask)
	    
	    bg_frame = cv2.bitwise_or(bg, bg, mask = mask)
	    new_frame = cv2.bitwise_or(frame, frame, mask = mask_inv)
	    
	    result = bg_frame + new_frame

	    cv2.imshow('mask', mask)
	    cv2.imshow('result', result)
	    k = cv2.waitKey(5) & 0xFF
	    if k == 27:
	        break
	    
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()