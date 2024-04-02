import os
import cv2


path = "Images2"

images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
count = len(images)

frame=cv2.imread(images[0])

height,width,channels=frame.shape
size = (width, height)
print(size)

out=cv2.VideoWriter('Project.mp4', cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)

for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()

print("done")    