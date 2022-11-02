import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from pymsgbox import *

vid = cv2.VideoCapture('video.mp4')
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    # print(label)
    if ("knife" in label or "scissors" in label):
        alert(text='Intruder alert a person is carrying harmful object', title='Alert', button='OK')
        vid.release()
        cv2.destroyAllWindows()
        break
        
    # Display the resulting frame
    cv2.namedWindow("Video frame", cv2.WINDOW_NORMAL)
  
    # Using resizeWindow()  
    cv2.resizeWindow("Video frame", 1200, 900)
    cv2.imshow('Video frame', frame)
      
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
  
# After the loop release the cap objectq
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
