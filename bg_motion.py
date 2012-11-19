import cv2 
import cv2.cv as cv
import sys
 
if __name__ == '__main__':
	if len(sys.argv) != 2:                                         ## Check for error in usage syntax
		print "Usage : python bg_motion.py <video>"
	else:
		video = sys.argv[1]
		
		cap = cv2.VideoCapture(video)
		cv2.namedWindow("input video") 
		
		retval_bg, bg = cap.read()
		bg_gray = cv2.cvtColor(bg, cv.CV_BGR2GRAY)
		
		cv2.namedWindow("motion detected")

		retval = True

		while retval: 
			retval, image = cap.read()
    			if retval:
        			image_gray = cv2.cvtColor(image, cv.CV_BGR2GRAY)

				diff = cv2.absdiff(bg_gray, image_gray)
	
				retval_diff, dst = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY);

				cv2.imshow("input video", image)
        			cv2.imshow("motion detected", dst)
    		 
    				key = cv2.waitKey(30)
		cv2.destroyAllWindows()
