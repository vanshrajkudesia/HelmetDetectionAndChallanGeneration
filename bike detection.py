from roboflow import Roboflow
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
b=bike_detection("download.jpg")
if b['predictions'][0]['class']=='motorcycle':
    h=helmet_detect("download.jpg")
    if h['predictions'][0]['class']=='Without Helmet':
        print("helmet not detected")
    
