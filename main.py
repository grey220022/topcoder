import sys
import os
import cv2

import shutil

if len(sys.argv)!=2:
  print("Command not valid. Please use command python3 main.py [filename]")
  sys.exit(1)

print(sys.argv[1])
current_directory = os.getcwd()
temp_directory = os.path.join(current_directory, r'temp_folder')

if os.path.exists(temp_directory):
   shutil.rmtree(temp_directory)

os.makedirs(temp_directory)
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite(temp_directory+"/frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
