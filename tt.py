#เทสกิฟให้เป็นพิกเซลแบบไม่ฟิคไซต์

from PIL import Image, ImageSequence

# Open the GIF file
gif = Image.open("C1Gif.gif")  # Replace "dog.gif" with your GIF file

# Define the pixel size for pixelation
pixel_size = 10  # Adjust this to change the level of pixelation

# Create a list to store the individual frames
frames = []

# Iterate through the frames of the GIF and pixelate each frame
for frame in ImageSequence.Iterator(gif):
    # Get the current frame as an image
    image = frame.copy()

    # Calculate the new size to pixelate the frame
    width, height = image.size
    new_width = width // pixel_size
    new_height = height // pixel_size

    # Resize the frame to pixelate it
    image = image.resize((new_width, new_height), Image.NEAREST)

    # Resize the frame back to its original size to get the pixelated effect
    image = image.resize((width, height), Image.NEAREST)

    # Append the pixelated frame to the list
    frames.append(image)

# Save the pixelated frames as a new GIF
frames[0].save("pixel_dog.gif", save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0)
