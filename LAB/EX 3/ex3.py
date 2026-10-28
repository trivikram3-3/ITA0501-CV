import cv2
import os

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
else:
    cv2.imshow("Input Image", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    folder = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(folder, "canny_edges.jpg")

    cv2.imwrite(output, edges)

    cv2.imshow("Canny Edge Image", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Output saved as canny_edges.jpg")
