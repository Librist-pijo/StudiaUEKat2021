from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

def main():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    # loop over the image paths
    for imagePath in paths.list_images("images/"):

        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=min(600, image.shape[1]))
        orig = image.copy()

        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)

        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

        filename = imagePath[imagePath.rfind("/") + 1:]
        print("[INFO] {} people were detected in the {}".format(
            len(pick), filename))

        cv2.imshow(f"{filename}", image)
        cv2.waitKey(0)
