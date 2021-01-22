import cv2


def get_filter_img(image,action):
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if action=="NO_FILTER":
        filtered = img
    elif action == "COLORIZED":
        filtered = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    elif action == "GRAYSCALE":
        filtered = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    elif action == "BINARY":
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        _,filtered = cv2.threshold(gray,100,250,cv2.THRESH_BINARY)
        print(_)
        print(filter)
    elif action == "INVERT":
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        _,binary = cv2.threshold(gray,100,250,cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(binary)
    elif action == "BLURED":
        width,height = img.shape[:2]
        if width>500:
            kernal = (25,25)
        elif width>200 or width<500:
            kernal = (15,15)
        blur = cv2.blur(img,kernal)
    return filtered 

