import cv2

# read image file
src_img = cv2.imread("lenna.jpg")
# convert gray scale
gray_img = cv2.cvtColor(src_img, cv2.COLOR_RGB2GRAY)
# read Harar
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = cascade.detectMultiScale(gray_img, scaleFactor = 1.2, minNeighbors = 2, minSize = (10, 10))

print(face_rect)

if len(face_rect) > 0:
	num = 0
	for rect in face_rect:
		x = rect[0]
		y = rect[1]
		width = rect[2]
		height = rect[3]
		dst_img = src_img[y : y + height, x : x + width]
		cv2.imwrite("./faces/trim_" + str(num) + ".jpg", dst_img)
		num += 1
else:
	print("No faces")
