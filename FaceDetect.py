import cv2
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



# attempting target priority:
priority = [] # list for holding confidence values
targets = [] # list for holding the targets that pass the confidence threshold

# Finding candidates that meets confidence threshold
for i in range(0, len(faces[1])):
    if faces[1][i][0] > 75:
        priority.append(faces[0][i][2] * faces[0][i][3] * faces[1][i][0])
        targets.append(faces[0][i])

 # Finding the largest target box, ie the closest target due to perspective geometry
closestTarget = max(priority)
targetNumber = priority.index(closestTarget)

target = faces[0][targetNumber] # Actual target to pass on from aimbot.

for j in range(0, len(priority)):
    print(f"Target priority: {priority[j]}, Target confidence: {faces[1][j][0]}")

print(f"Found {len(targets)} targets!")

print(target)

# Prepping to draw target box:
upperLeft = (target[0], target[1]) # Upper left corner of target box
lowerRight = (target[0]+target[2], target[1]+target[3]) # lower right corner of target box.

cv2.rectangle(image, upperLeft, lowerRight, (0, 255, 0), 2)

# Draw a rectangle around the faces
# for (x, y, w, h) in target:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow("Faces found", image)
cv2.waitKey(0)
