import easyocr
import cv2
import csv
from matplotlib import pyplot as plt
reader = easyocr.Reader(['ar'],gpu=False)
img = cv2.imread("C:\\Users\\seife\\OneDrive\\Desktop\\plate numers\\Egypt_-_License_Plate_-_Private_Cairo.png")
img2 = cv2.imread("C:\\Users\\seife\\OneDrive\\Desktop\\plate numers\\plate3.jpg")

#crop image using opencv
cropped  = img[110:250,0:500]
plt.subplot(1,4,1)
plt.imshow(cropped )
cropped2  = img2[250:540,0:]
plt.subplot(1,4,2)
plt.imshow(cropped2)

#using ocr to detect characters
results = reader.readtext(cropped,detail=True,paragraph=False)
results2 = reader.readtext(cropped2,detail=True,paragraph=False)

#filter the output
text = ''
for result in results:
    text +=result[1]+' '
print (text)

text2 = ''
for result in results2:
    text2 +=result[1]+' '
print (text2)
with open ('fil.csv','w') as f:
    f.write(f"{text}\n") 
    f.write(f"{text2}\n") 

   
plt.show()   

