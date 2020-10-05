import cv2

# load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('imagename...')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detect face
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (a, b, w, h) in faces:
    cv2.rectangle(img, (a, b), (a + w, b + h), (0, 0, 255), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
