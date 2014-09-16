__author__ = 'archer'
import datetime

class FrameMetadata:

     def __init__(self, data):
         self.datetime = datetime.datetime.now()
         self.camera_metadata = data
         """

         :return:
         """