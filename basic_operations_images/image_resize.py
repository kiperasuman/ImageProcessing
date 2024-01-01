import cv2
import numpy
import matplotlib

#imread, flag kısmına 0 yazarsam gri hale çevirir
image = cv2.imread("image_processing.jpeg", 0)
# print(image)

cv2.namedWindow("Yapay Zeka Temelleri Pencere Buyutme ",cv2.WINDOW_NORMAL)
cv2.imshow("Yapay Zeka Temelleri Pencere Buyutme ",image)

#resmi kaydetme işlemi (proje dosyalarına kayıt edilir)
cv2.imwrite("C:/Users/Kullanici/Downloads/image_processing.jpeg",image)

#peki dosyanın yolunu farklı verirsek uzantı olarak


cv2.waitKey(0) #ben kapatana kadar açık kalır 1000 ms 1 sn
cv2.destroyAllWindows() # q tuşuna basınca hepsi kapanır