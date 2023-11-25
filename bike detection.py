from roboflow import Roboflow
import cv2
def bike_detection(image):

    rf = Roboflow(api_key="MW6fsjVoDPJTTqTzDOp6")
    project = rf.workspace().project("motorcycle-xjypd")
    model = project.version(1).model

    # infer on a local image
    print(model.predict(image, confidence=40, overlap=30).json())
    detected_bike=model.predict(image, confidence=40, overlap=30).json()
    return detected_bike
def helmet_detect(image):
    rf = Roboflow(api_key="MW6fsjVoDPJTTqTzDOp6")
    project = rf.workspace().project("bike-helmet-detection-2vdjo")
    model = project.version(1).model

    # infer on a local image
    print(model.predict(image, confidence=40, overlap=30).json())
    detected_helmet=model.predict(image, confidence=40, overlap=30).json()
    return detected_helmet

    # visualize your prediction
    #model.predict("helmet1.jpg", confidence=40, overlap=30).save("prediction.jpg")
# visualize your prediction
#model.predict("download.jpg", confidence=40, overlap=30).save("prediction.jpg")
b=bike_detection("bike.jpg")
if b['predictions'][0]['class']=='motorcycle':
    h=helmet_detect("bike.jpg")
    if h['predictions'][0]['class']=='Without Helmet':
        print("helmet not detected")
img=cv2.imread("bike.jpg")
width=1300
height=1000
crop_width = 1037
crop_height = 806
x = (width - crop_width) // 2
y = (height - crop_height) // 2
crop_rectangle = (x, y, x + crop_width, y + crop_height)

# Crop the image
cropped_image = img[crop_rectangle[1]:crop_rectangle[3], crop_rectangle[0]:crop_rectangle[2]]

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)