import sys
import os
import cv2
import shutil

#get frame per second for the video
def getfps(filename):
    video = cv2.VideoCapture(filename);
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
    video.release(); 
    return fps

if len(sys.argv)!=2:
  print("Command not valid. Please use command python3 main.py [filename]")
  sys.exit(1)


print(sys.argv[1])
fps=getfps(sys.argv[1])
current_directory = os.getcwd()
temp_directory = os.path.join(current_directory, r'temp_folder')

#remove temp folder if it exists
if os.path.exists(temp_directory):
   shutil.rmtree(temp_directory)

#create temp folder
os.makedirs(temp_directory)
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  if (count % fps==0):
    time=count/fps
#image sampling from video
    cv2.imwrite(temp_directory+"/frame%d.jpg" % time, image)     # save frame as JPEG file
  count += 1

#remove temp folder
if os.path.exists(temp_directory):
   shutil.rmtree(temp_directory)

