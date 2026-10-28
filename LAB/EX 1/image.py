import cv2
import os


image = cv2.imread("image.jpg")


if image is None:
    print("Image not found!")
else:

    cv2.imshow("Input Image", image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    folder = os.path.dirname(os.path.abspath(__file__))

    output_path = os.path.join(folder, "gray_image.jpg")
    cv2.imwrite(output_path, gray)

    cv2.imshow("Grayscale Image", gray)

    print("Grayscale image saved at:")
    print(output_path)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
