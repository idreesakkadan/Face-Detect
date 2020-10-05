import cv2
# load cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('imagename...')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (a, b, w, h) in faces:
    cv2.rectangle(img, (a, b), (a + w, b + h), (0, 0, 255), 2)

cv2.
