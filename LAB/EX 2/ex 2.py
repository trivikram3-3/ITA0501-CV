import cv2
import os


image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
else:
   
    cv2.imshow("Input Image", image)

    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    folder = os.path.dirname(os.path.abspath(__file__))

    output_path = os.path.join(folder, "blurred_image.jpg")
    cv2.imwrite(output_path, blurred)

    cv2.imshow("Gaussian Blurred Image", blurred)

    print("Blurred image saved at:")
    print(output_path)

    cv2.waitKey(0)

    cv2.destroyAllWindows()
