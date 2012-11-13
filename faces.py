import cv2
import cv2.cv as cv
import sys

def detect(img, cascade):
	rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10), flags = cv.CV_HAAR_SCALE_IMAGE)
	if len(rects) == 0:
		return []
	rects[:,2:] += rects[:,:2]
	return rects

def draw_rects(img, rects, color):
	for x1, y1, x2, y2 in rects:
		cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
	if len(sys.argv) != 2:                                         ## Check for error in usage syntax
		print "Usage : python faces.py <image_file>"

	else:
		img = cv2.imread(sys.argv[1],cv2.CV_LOAD_IMAGE_COLOR)  ## Read image file

		if (img == None):                                      ## Check for invalid input
			print "Could not open or find the image"
		else:
			cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
			gray = cv2.cvtColor(img, cv.CV_BGR2GRAY)
			gray = cv2.equalizeHist(gray)
	
			rects = detect(gray, cascade)
			
			## Extract face coordinates			
			x1 = rects[0][1]
			y1 = rects[0][0]
			x2 = rects[0][3]
			y2 = rects[0][2]
			
			## Extract face ROI
			faceROI = gray[x1:x2, y1:y2]

			## Show face ROI
			cv2.imshow('Display face ROI', faceROI)

			vis = img.copy()
			draw_rects(vis, rects, (0, 255, 0))

        		cv2.namedWindow('Display image')          ## create window for display
        		cv2.imshow('Display image', vis)          ## Show image in the window

        		print "size of image: ", img.shape        ## print size of image
        		cv2.waitKey(0)                            ## Wait for keystroke
        		cv2.destroyAllWindows()                   ## Destroy all windows
