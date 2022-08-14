import easyocr
import cv2
import csv
from matplotlib import pyplot as plt
reader = easyocr.Reader(['ar'],gpu=False)
img = cv2.imread("C:\\Users\\seife\\OneDrive\\Desktop\\plate numers\\plate car 2.webp")
img2 = cv2.imread("C:\\Users\\seife\\OneDrive\\Desktop\\plate numers\\plate3.jpg")

#filtring and noise removal image of image 1 using opencv
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
bfilter = cv2.bilateralFilter(gray,11,17,17)
edged = cv2.Canny(bfilter,30,200)
plt.subplot(1,4,1)
plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB) )
#crop image 2
cropped2  = img2[250:540,0:]
plt.subplot(1,4,2)
plt.imshow(cropped2)

#using ocr to detect characters
results = reader.readtext(gray,detail=True,paragraph=False)
results2 = reader.readtext(cropped2,detail=True,paragraph=False)

#filter the output
text = ''
for result in results:
    text +=result[1]+' '
print (text)

text2 = ''
for result2 in results2:
    text2 +=result2[1]+' '
print (text2)
with open ("C:\\Users\\seife\\OneDrive\\Desktop\\plate numers\\fil.csv",'w') as f:
    f.write(f"{text}\n") 
    f.write(f"{text2}\n") 
plt.show()   

