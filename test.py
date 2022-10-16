import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from keras.models import load_model
from PIL import Image, ImageOps



facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
font=cv2.FONT_HERSHEY_COMPLEX


model = load_model('keras_model2.h5', compile=False)


def get_className(classNo):
	if classNo==0:
		return "tarun"
	elif classNo==1:
		return "surya"

while True:
	success, imgOriginal=cap.read()
	cv2.imwrite("frame.jpg", imgOriginal)
	faces = facedetect.detectMultiScale(imgOriginal, 1.3, 5)
	for x,y,w,h in faces:
		data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

		image = Image.open('frame.jpg').convert('RGB')

		# resize the image to a 224x224 with the same strategy as in TM2:
		# resizing the image to be at least 224x224 and then cropping from the center
		size = (224, 224)
		image = ImageOps.fit(image, size, Image.ANTIALIAS)

		# turn the image into a numpy array
		image_array = np.asarray(image)

		# Normalize the image
		normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

		# Load the image into the array
		data[0] = normalized_image_array

		# turn the image into a numpy array
		image_array = np.asarray(image)
		# Normalize the image
		normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

		# Load the image into the array
		data[0] = normalized_image_array

		# run the inference
		prediction = model.predict(data)

		classIndex=np.argmax(prediction)
		probabilityValue=np.amax(prediction)
		cv2.rectangle(imgOriginal, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cv2.rectangle(imgOriginal, (x, y - 40), (x + w, y), (0, 255, 0), -2)
		cv2.putText(imgOriginal, str(get_className(classIndex)), (x, y - 10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)

		cv2.putText(imgOriginal, str(round(probabilityValue * 100, 2)) + "%", (180, 75), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
	cv2.imshow("Result", imgOriginal)
	k=cv2.waitKey(1)
	if k==ord('q'):
		break


cap.release()
cv2.destroyAllWindows()





















