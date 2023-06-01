import cv2
import numpy as np
import sys
import PIL
from PIL import Image



def main():
	"""
	Main program
	"""
	#print(sys.argv)

	firstwindow= "Source"
	secondwindow= "Source 2"
	cv2.namedWindow(firstwindow, cv2.WINDOW_NORMAL)
	cv2.namedWindow(secondwindow, cv2.WINDOW_NORMAL)
	
	
	
	# 1. GrayScale using weighted averages
	# Averages are Red = 0.299, Blue = 0.587, and Green = 0.114.

	# load two source paths in cmd because this function tries two different RGB values.

	def grayScale():
		print("Running grayScale function")
		src1 = cv2.imread(sys.argv[1])
		cv2.imshow("Source", src1)
		cv2.waitKey(0)

		(rows, cols) = src1.shape[0:2]

		for i in range(rows):
    			for j in range(cols):
        		# Find the average of the RBG values which is equal to 0.333
        			src1[i, j] = sum(src1[i, j]) * 0.333

		cv2.imshow('grayscale1.png', src1)
		cv2.imwrite('grayscale1.png', src1)
		cv2.waitKey(0)

		# Using other image and different values
		# Averages are Red = 0.399, Blue = 0.487, and Green = 0.214.

		src2 = cv2.imread(sys.argv[2])
		cv2.imshow("Source 2", src2)
		cv2.waitKey(0)

		(rows, cols) = src2.shape[0:2]

		for i in range(rows):
    			for j in range(cols):
        			src2[i, j] = sum(src2[i, j]) * 0.366


		cv2.imshow('grayscale2.png', src2)
		cv2.imwrite('grayscale2.png', src2)
		cv2.waitKey(0)
		print("Completed grayScale function. Image is saved")
	

	
	

	# 2. Thresholding

	# Could not load image from command line, please enter the image path for this function at im_gray line.

	def thresholding():
		print("Running threshold function")
		grayScaleImage = cv2.imread(sys.argv[1])
		cv2.imshow("Source", grayScaleImage)
		cv2.waitKey(0)
		im_gray = np.array(PIL.Image.open("grayscale1.png").convert('L'))
		print(type(im_gray))

		thresholdValue = int(input("Enter Threshold Value:"))
		(rows, cols) = grayScaleImage.shape[0:2]
	
		bool = im_gray > thresholdValue
		print(bool)

		maximumValue = 255
		im_bin = (im_gray > thresholdValue) * maximumValue
		print(im_bin)
	
		Image.fromarray(np.uint8(im_bin)).save('black&white.png')
		print("Completed threshold function. Image is saved")
	

	# 3. Padding

	# Could not load image from command line, please enter the image path for this function at im_in line.

	def padding():
		print("Running padding function")	
		grayScaleImage = cv2.imread(sys.argv[1])
		cv2.imshow("Source", grayScaleImage)
		cv2.waitKey(0)

		img_in = Image.open("grayscale1.png")
		array = np.array(img_in)

		(rows, cols) = grayScaleImage.shape[0:2]
		padded_array = np.pad(array, ((10, 10), (10, 10), (0, 0)))

		img_out = Image.fromarray(padded_array)
		img_out.save('paddedImage.png')

	
	
		"""
		#using BORDER_CONSTANT 

		paddingValue = int(input("Enter Padding Value:"))
		paddedImage = cv2.copyMakeBorder(grayScaleImage, paddingValue, paddingValue, paddingValue, paddingValue, cv2.BORDER_CONSTANT, (0,0,0))
		cv2.imshow("paddedimg.png", paddedImage)
		cv2.imwrite("paddedimg.png", paddedImage)
		cv2.waitKey(0)

		"""
		print("Completed padding function. Image is saved")

	
	# 4. Blurring

	def blurring():
		print("Running blurring function")
		grayScaleImage = cv2.imread(sys.argv[1])
		cv2.imshow("Source", grayScaleImage)
		cv2.waitKey(0)

		#using BORDER_CONSTANT 

		paddingValue = int(input("Enter Padding Value:"))
		paddedImage = cv2.copyMakeBorder(grayScaleImage, paddingValue, paddingValue, paddingValue, paddingValue, cv2.BORDER_CONSTANT, (0,0,0))
		cv2.imshow("paddedimg.png", paddedImage)
		#cv2.imwrite("paddedimgdup.png", paddedImage)
		cv2.waitKey(0)

		#blurring the duplicate zero padded image 
		#using uniform distribution kernel ([1, 1, 1], [1, 1, 1], [1, 1, 1]) to blur the image
	
		kernel = np.ones((3, 3), np.float32) / 9
		blurredImage = cv2.filter2D(paddedImage, -1, kernel)

		#blurredImage = cv2.blur(paddedImage,(5,5)) 
		cv2.imshow('blur.png',blurredImage)
		cv2.imwrite('blur.png',blurredImage)
		cv2.waitKey(0)
	
		print("Completed blurring function. Image is saved")

	
	# 5. Sharpening

	def sharpening():
		print("Running sharpening function")
		grayScaleImage = cv2.imread(sys.argv[1])
		cv2.imshow("Source", grayScaleImage)
		cv2.waitKey(0)

		#using BORDER_CONSTANT 

		paddingValue = int(input("Enter Padding Value:"))
		paddedImage = cv2.copyMakeBorder(grayScaleImage, paddingValue, paddingValue, paddingValue, paddingValue, cv2.BORDER_CONSTANT, (0,0,0))
		cv2.imshow("paddedimg.png", paddedImage)
		#cv2.imwrite("paddedimgdup.png", paddedImage)
		cv2.waitKey(0)
	
		k = np.array([[0, -1, 0],
	                    [-1, 5, -1],
	                    [0, -1, 0]])

		sharpImage= cv2.filter2D(src=paddedImage, ddepth=-1, kernel=k)

		cv2.imshow("sharp.png",sharpImage)
		cv2.imwrite("sharp.png",sharpImage)
		cv2.waitKey(0)
		print("Completed sharpening function. Image is saved")
	
	grayScale()
	thresholding()
	padding()
	blurring()
	sharpening()

if __name__ == "__main__":
	main()
	
