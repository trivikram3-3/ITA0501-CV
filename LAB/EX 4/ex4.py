import cv2
import os

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    folder = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(folder, "equalized_image.jpg")

    cv2.imwrite(output, equalized)

    print("Output saved as equalized_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
