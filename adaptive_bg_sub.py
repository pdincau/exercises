import cv2 
import cv2.cv as cv
import sys
 
if __name__ == '__main__':
	if len(sys.argv) != 2:                                         ## Check for error in usage syntax
		print "Usage : python adaptive_bg_sub.py <video>"
	else:
		video = sys.argv[1]

		# Define values for alpha and beta		
		alpha = 0.5
		beta = 1 - alpha

		cap = cv2.VideoCapture(video)
		cv2.namedWindow("input video") 

		# Read first frame from video and set it as reference frame		
		retval_bg, bg = cap.read()

		# Convert to gray level
		bg_gray = cv2.cvtColor(bg, cv.CV_BGR2GRAY)
		
		cv2.namedWindow("motion detected")

		retval = True

		# while we have frames in the video
		while retval: 
			retval, image = cap.read()
    			if retval:
				# Convert to gray level the current frame
        			image_gray = cv2.cvtColor(image, cv.CV_BGR2GRAY)

				# Compute difference with reference frame
				diff = cv2.absdiff(bg_gray, image_gray)
	
				# Threshold difference
				retval_diff, dst = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY);

				# Update background
				bg_gray = cv2.addWeighted(image_gray, alpha, bg_gray, beta, 0)
					
				cv2.imshow("input video", image)
        			cv2.imshow("motion detected", dst)
    		 
    				key = cv2.waitKey(30)
		cv2.destroyAllWindows()
