import cv2
import numpy as np
import imageConversion
# def contoursOfImage(image):

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Threshold the image to create a binary image
#     _, binary_image = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

#     # Find contours in the binary image
#     contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Draw contours on the original image (for visualization)
#     cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

#     # Display the result
#     cv2.imshow('Contours', image)
#     cv2.waitKey(1000)
#     cv2.destroyAllWindows()
#     print("image rendered")

def binaryImgToOpenCV(binaryData):
    # Convert Uint8ClampedArray to NumPy array
    uint8_array = binaryData["dataArray"]
    height = binaryData["height"]
    width = binaryData["width"]
    np_array = np.array(uint8_array, dtype=np.uint8)
    # Reshape the array to match the image dimensions
    np_array = np_array.reshape((height, width, 4))

    # Extract only the RGB channels (excluding alpha channel)
    rgb_array = np_array[:, :, :3]

    # Convert RGB to BGR (OpenCV uses BGR format)
    bgr_array = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2BGR)
    # contoursOfImage(bgr_array)

    return imageConversion.imageConverter(bgr_array)


# Display the image using OpenCV (you can use other methods for display as well)

