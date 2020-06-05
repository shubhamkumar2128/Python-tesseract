from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()

#while running provide image path like python testocr.py --image img.png
ap.add_argument("-i", "--image", required=True,	help="path to input image to be OCR'd") 
args = vars(ap.parse_args())

image = cv2.imread(args["image"])		#read image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #convert it to grayscale

#write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid())   
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))  #extract text from image
print(text)
os.remove(filename) #remove temporary file which we have created above


# show the output images
cv2.imshow("Image", image)  #orignal image	
cv2.imshow("Output", gray)  #image after extracting text
cv2.waitKey(0)
