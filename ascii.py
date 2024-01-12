from PIL import Image
import numpy as np

def map_char_to_intensity(char):
    """
    Simple heuristic to map a character to a grayscale intensity.
    This needs to be adjusted based on the characters used and desired effect.
    """
    return sum(ord(c) for c in char) % 256

def image_to_ascii_custom(image_path, grid_size, ascii_chars):
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.height / img.width
    new_width = grid_size
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # Create intensity map for each character
    char_intensity = {char: map_char_to_intensity(char) for char in ascii_chars}

    # Convert the grayscale image to numpy array
    pixels = np.array(img)

    # Create ASCII art
    ascii_art = ''
    for i in range(0, pixels.shape[0]):
        for j in range(0, pixels.shape[1]):
            avg_intensity = pixels[i, j]
            chosen_char = min(char_intensity, key=lambda char: abs(char_intensity[char] - avg_intensity))
            ascii_art += chosen_char
        ascii_art += '\n'

    return ascii_art

# Path to the image file
image_path = 'svenra.png'  # Replace with your image path

# Convert and print ASCII Art
ascii_art = image_to_ascii_custom(image_path, 50, "svenra")
print(ascii_art)
