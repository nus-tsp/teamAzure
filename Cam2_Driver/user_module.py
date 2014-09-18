__author__ = 'archer'
from analyzer import Analyzer
from frame_metadata import FrameMetadata
from camera_metadata import CameraMetadata
import datetime
import matplotlib.pyplot as plt
import numpy as np

import cv2

class MyAnalyzer(Analyzer):

 def initialize(self):

    self.__results = {}
    self.__index = {}
    self.__images = []
    self.final_results = {}

 def on_new_frame(self):

    images = self.get_new_frames()
    i = 0
    for image in images:
        self.__images.append(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

        hist = cv2.calcHist([image],[0,1,2],None,[64,64,64],[0,256,0,256,0,256])
        hist = cv2.normalize(hist).flatten()
        self.__index[i] = hist
        i = i + 1

    for (k,hist) in self.__index.items():
        d = cv2.compareHist(self.__index[0],hist,cv2.cv.CV_COMP_CORREL)
        self.__results[k] = d

    self.__results = sorted([(hist,k)for (k,hist)in self.__results.items()],reverse = True)

 def finalize(self):
    fig = plt.figure("Doge")

    ax = fig.add_subplot(1,1,1)
    ax.imshow(self.__images[0])
    plt.axis("off")

    fig = plt.figure("correlation")

    for(i,(hist,k)) in enumerate(self.__results):
        print k
        print hist
        ax = fig.add_subplot(1, len(self.__images), i + 1)
        plt.imshow(self.__images[k])
        plt.axis("off")

    plt.show()

