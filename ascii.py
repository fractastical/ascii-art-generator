from PIL import Image
import numpy as np

def image_to_ascii(image_path, grid_size, ascii_chars):
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.height / img.width
    new_width = grid_size
    new_height = aspect_ratio * new_width * 0.5
    img = img.resize((new_width, int(new_height)))

    # Convert image to grayscale
    img = img.convert("L")

    # Convert the grayscale image to numpy array
    pixels = np.array(img)

    # ASCII characters to use (cycling through 'ascii_chars')
    ascii_str = ''
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            ascii_str += ascii_chars[(i * pixels.shape[1] + j) % len(ascii_chars)]
        ascii_str += '\n'

    return ascii_str

# Path to the image file
image_path = 'path_to_your_image.png'  # Replace with your image path

# Convert and print ASCII Art
ascii_art = image_to_ascii(image_path, 50, "svenra")
print(ascii_art)
