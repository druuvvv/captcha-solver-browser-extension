import cv2
import numpy as np

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
    # cv2.imshow('Converted Image', bgr_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return bgr_array


# Display the image using OpenCV (you can use other methods for display as well)

