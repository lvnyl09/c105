import os
import cv2

path = 'Images/'
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.jpg', '.jpeg', '.png']:
        file_name = os.path.join(path, file)
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

video_name = 'Project.avi'
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
vid = cv2.VideoWriter(video_name, fourcc, fps, size)

for i in range(count):
    image = cv2.imread(Images[i])
    vid.write(image)

vid.release()
print("Done")
