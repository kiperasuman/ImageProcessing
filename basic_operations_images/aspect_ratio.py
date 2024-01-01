import cv2

def resizeWithAspectRatio(img,width=None,height=None , inter=cv2.INTER_AREA):
    dimension = None
    (h,w) = img.shape[:2]
    print(h,w)
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w*r) , height)
    else:
        r = width /float(w)
        dimension = (width , int(h*r))

    print(dimension)
    return cv2.resize(img,dimension , interpolation= inter)

image = cv2.imread("D:/pythonProjects/first_app/basic_operations_images/image_processing.jpeg")

cv2.imshow("Original Image",image)
cv2.imshow("Aspect Ratio",resizeWithAspectRatio(image,1500,None))

cv2.waitKey(0)
cv2.destroyAllWindows()