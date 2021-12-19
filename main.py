try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


print(pytesseract.image_to_string(Image.open('testNapis.png')))


img1 = cv2.imread('sensors-20-01495-g004.png')
scale_percent = 30  # percent of original size
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('normal img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
img_convert1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
converted_img = cv2.threshold(cv2.GaussianBlur(img_convert1, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('gausian', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img2 = cv2.imread('4-Figure3-1.png')
img_convert2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('normal img', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.threshold(cv2.GaussianBlur(img_convert2, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('gausian', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.threshold(cv2.bilateralFilter(img_convert1, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('bilateral', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.threshold(cv2.bilateralFilter(img_convert2, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('bilateral', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.threshold(cv2.medianBlur(img_convert1, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('medianBlur', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.threshold(cv2.medianBlur(img_convert2, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('medianBlur', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
##Kolejne 3
converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img_convert1, (5, 5), 0),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('GaussianBlurAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.adaptiveThreshold(cv2.GaussianBlur(img_convert2, (5, 5), 0),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('GaussianBlurAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img_convert1, 9, 75, 75),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('bilateralFilterAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.adaptiveThreshold(cv2.bilateralFilter(img_convert2, 9, 75, 75),
                                      255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('bilateralFilterAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img_convert1, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('medianBlurAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
converted_img = cv2.adaptiveThreshold(cv2.medianBlur(img_convert2, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
cv2.imshow('medianBlurAdapt', converted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

