
import datetime
import numpy as np
import cv2
import glob
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("data", help = "Path")
args = vars(parser.parse_args())

#inputfile = open('input', "w")
outputfile = open('output', "w")

for imagePath in glob.glob(args["data"]+"/*.png"):
	# Get the frame
	#print imagePath
	filename = imagePath[imagePath.rfind("/")+1:]
	frame = cv2.imread(imagePath)
	print filename
        # Create a new array the same size as frame and fill with zeros
        white = np.zeros_like(frame,np.uint8)

        # Fill all values of array with 255 to make white image
        white.fill(255)

        # Subtract img from white to invert image
        inverted_frame = white - frame
	
	cv2.imwrite("out.png",inverted_frame);
        # Save frame to a file with prefix "input_"
        #inputfile.write(frame)

        # Save result in a file with prefix "result_".
        outputfile.write(frame)

#inputfile.close()
outputfile.close()
