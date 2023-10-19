#เทสรูปปกติให้เป็นพิกเซลแบบง่ายๆ

from PIL import Image

# Load the dog image
image = Image.open("2.jpg")  # Replace "dog.jpg" with your image file

# Define the pixel size for pixelation
pixel_size = 10  # Adjust this to change the level of pixelation

# Calculate the new size to pixelate the image
width, height = image.size
new_width = width // pixel_size
new_height = height // pixel_size

# Resize the image to pixelate it
image = image.resize((new_width, new_height), Image.NEAREST)

# Resize the image back to its original size to get the pixelated effect
image = image.resize((width, height), Image.NEAREST)

# Save the pixelated image
image.save("pixel_dog.jpg")  # Save to a new file
