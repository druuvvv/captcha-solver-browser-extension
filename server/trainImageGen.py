from PIL import Image, ImageDraw, ImageFont
import random
import string
import numpy as np
import os

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def func():
  font_files = [f for f in os.listdir("/fonts") if f.endswith('.ttf')]
  # Create a blank image with a white background
  image = Image.new('L', (30, 30), 'black')
  draw = ImageDraw.Draw(image)

  # Generate a random letter
  random_letter = random.choice(string.ascii_letters + "1234567890@=")

  # Choose a bigger font size
  font_size = 30
  font = ImageFont.truetype(random.choice(font_files), font_size)

  # Calculate the vertical position to touch the bottom margin
  text_position = ((30 - draw.textbbox((0, 0), random_letter, font=font)[2]) // 2, 30 - draw.textbbox((0, 0), random_letter, font=font)[3])

  # Draw the letter on the image
  draw.text(text_position, random_letter, font=font, fill='white')
  # Convert the image to a NumPy array
  image_array = np.array(image)

    # Apply binary thresholding to create a binary image
  new_array = np.where(image_array < 128 , 0 , image_array)
  newer_array = np.where(new_array >=128 , 255 , new_array)

  image.save("testing/"+random_letter +"_" + generate_random_string(4) +  ".png")
  image.save(random_letter +"_" + generate_random_string(4) +  ".png")




func()