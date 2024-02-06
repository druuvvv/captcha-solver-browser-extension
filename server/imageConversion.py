import cv2
import numpy as np
import bfs
import pytesseract

def imageConverter(img):
    # Convert to grayscale
    c_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Median filter
    kernel = np.ones((3,3),np.uint8)
    out = cv2.medianBlur(c_gray,3)
    # Image thresholding 
    print(out.shape)
    new_array = np.where(out < 180 , 0 , out)
    newer_array = np.where(new_array >=180 , 255 , new_array)

    # Islands removing with threshold = 30
    out = bfs.removeIsland(newer_array, 30)
    # Median filter
    out = cv2.medianBlur(out,3)

    contours, _ = cv2.findContours(out, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        # Crop to content
        cropped_image = out[y:y+h, x:x+w]

        padded_image = cv2.copyMakeBorder(cropped_image, 15, 0, 9, 9, cv2.BORDER_CONSTANT, value=0)
        # Resize to (30, 30)
        scaled_image = cv2.resize(padded_image, (30, 30))
        print(scaled_image.shape)
        cv2.imshow('out',scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        result = model.predict(padded_image)
        print(result)
        predicted_index = result.argmax(axis=1)[0]  # Get the index of the predicted class
        predicted_char = stri[predicted_index]
        print(predicted_char)
    return pytesseract.image_to_string(out)
    