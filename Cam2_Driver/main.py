from user_module import MyAnalyzer
from camera_metadata import CameraMetadata
from frame_metadata import FrameMetadata
import cv2
import time

def fetch_snapshots_sync(analyzer):
    """
    Simulate fetching images in group of camera_count, give it to analyzer
    """

    frames = []
    frame_metadata = []

    frames.append(cv2.imread('Images/img1.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[0]))
    frames.append(cv2.imread('Images//img2.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[1]))
    frames.append(cv2.imread('Images//img3.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[2]))
    frames.append(cv2.imread('Images//img4.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[3]))
    frames.append(cv2.imread('Images//img5.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[4]))


    frame_temp = []
    frame_metadata_temp = []

    for i in range(1):
        frame_temp.append(frames)
        frame_metadata_temp.append(frame_metadata)
        analyzer.receive_frames(frame_temp,frame_metadata_temp)
        analyzer.on_new_frame()
        #time.sleep(running_time/snapshot_interval)

def fetch_snapshots_async(analyzer):
    """
    Simulate fetching images and give it to analyzer
    """
    frames = []
    frame_metadata = []
    frames.append(cv2.imread('Images/img1.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[0]))
    frames.append(cv2.imread('Images//img2.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[1]))
    frames.append(cv2.imread('Images//img3.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[2]))
    frames.append(cv2.imread('Images//img4.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[3]))
    frames.append(cv2.imread('Images//img5.jpg', cv2.CV_LOAD_IMAGE_COLOR))
    frame_metadata.append(FrameMetadata(camera_list[4]))



    frame_temp = []
    frame_metadata_temp = []
    for i in range(5):
        frame_temp.append(frames[i])
        frame_metadata_temp.append(frame_metadata[i])
        analyzer.receive_frames(frame_temp, frame_metadata_temp)
        analyzer.on_new_frame()

#Get configuration from database, setup analyzer

def fake_camera_metadata_generator(cid):
    lat = 1.0
    lon = 103.8
    camera_metadata = CameraMetadata(cid,lat,lon)

    return camera_metadata

def get_camera_list(cid_list):
    camera_list = []
    for i in range(len(cid_list)):
        camera_list.append(fake_camera_metadata_generator(cid_list[i]))

    return camera_list

cid_list = [123, 154, 177, 166, 104] #Random assigned camera id which is supposed to be read from database
camera_count = 5
maximum_snapshots_to_keep = 3
running_time = 30
snapshot_interval = 5
sync = True

analyzer = MyAnalyzer(camera_count, maximum_snapshots_to_keep)
analyzer.initialize()
camera_list = get_camera_list(cid_list)

#if analyzer.sync is true, fetch camera snapshots in group, wait until all snapshots are available

#when new frame is received from the system
if not sync:
    fetch_snapshots_async(analyzer)
else:
    fetch_snapshots_sync(analyzer)


#finalize
analyzer.finalize()


