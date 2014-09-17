__author__ = 'archer'

class Analyzer:

    def __init__(self, c_count, max_to_keep):
        self.__c_count = c_count
        self.__frames = [[0 for x in xrange(c_count)] for x in xrange(max_to_keep)]
        self.__max_to_keep = max_to_keep


    def on_new_frame(self):
        """
        Called when new frame is ready

        """

    def initialize(self):
        """
        Called when analyzer object is created

        """

    def finalize(self):
        """
        Called when snapshot analysis is finished, to handle data formatting or saving files

        """

    def get_new_frames(self):
        """
        To get new frames, act synchronously or asynchronously
            sync = true:
                return the frames until a group of frames are available
            sync = false:
                return the newest frame when a new frame is ready

        return type: frame[]

        """
        last_index = len(self.__frames) - 1
        return self.__frames[last_index]

    def get_frame(self, *args):
        """
        Load nth previous frame from the camera with cid:
        TODO
        """
        if (not len(args)):
            last_index = len(self.__frames) - 1
            return self.__frames[last_index]
        elif (len(args == 1)):
            return self.__frames[args[0]]


    def get_frame_metadata(self):
        """
        TODO
        """
        last_index = len(self.__frame_metadata) - 1
        return self.__frame_metadata[last_index]


    def save(self, path, file):
        """

        To save the file in path

        """
    def get_camera_count(self):
        return self.__c_count


    def receive_frames(self, frames, frame_metadata):
        self.__frames = frames
        self.__frame_metadata = frame_metadata