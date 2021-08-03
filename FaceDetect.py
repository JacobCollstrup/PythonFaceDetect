import cv2
import sys

# Get user supplied values
imagePath = "abba.png"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale2(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces[0])))

print(faces[0])
print(faces[1])

print((faces[0][0][1]))

print(len(faces[1]))

# attepmting target priority:
priority = []
for i in range(0, len(faces[1])):
    priority.append(faces[0][i][2] * faces[0][i][3] * faces[1][i][0])

for j in range(0, len(priority)):
    print(f"Target priority: {priority[j]}")

# Draw a rectangle around the faces
for (x, y, w, h) in faces[0]:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
