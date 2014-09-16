__author__ = 'archer'
from analyzer import Analyzer
from frame_metadata import FrameMetadata
from camera_metadata import CameraMetadata
import datetime

import numpy as np

import cv2

class MyAnalyzer(Analyzer):

 def initialize(self):


     # Initialize statistics

     self.motion_frames = 0

     self.total_frames = 0

     self.total_motion = 0

     self.output_text = ''

 def on_new_frame(self):

     # Get frame

     frame = self.get_frame()

     # Get frame metadata

     frame_metadata = self.get_frame_metadata()

     # Get date/time of frame, time is UTC

     datetime = frame_metadata.datetime.strftime('%Y-%m-%d_%H-%M-%S')

     # Get camera id

     camera_id = frame_metadata.camera_metadata.camera_id

     # Apply background subtraction to frame


     # Calculate percent of mask that is foreground


     # Add frame percentage to total, used to calculate average percent motion


     # Count frame as containing motion if percent motion is greater than 0.5%



     # Increment the total number of frames


 def finalize(self):
    """

    :return:
    """