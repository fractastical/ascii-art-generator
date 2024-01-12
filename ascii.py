from PIL import Image, ImageDraw, ImageFont
import numpy as np

def map_char_to_intensity(char):
    """
    Simple heuristic to map a character to a grayscale intensity.
    This needs to be adjusted based on the characters used and desired effect.
    """
    return sum(ord(c) for c in char) % 256

def get_ascii_char(value, ascii_chars):
    """
    Map a grayscale value to an ASCII character.
    """
    return ascii_chars[int(value / 256 * len(ascii_chars))]

def get_ascii_char(value):
    """
    Map a grayscale value to an ASCII character.
    """
    ascii_chars = "@%#*+=-:. "  # Darker to lighter
    return ascii_chars[int(value / 256 * len(ascii_chars))]

def image_to_ascii(image_path, grid_size):
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.height / img.width
    new_width = grid_size
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # ASCII characters ordered by perceived luminance
    ascii_chars = "@%#*+=-:. "  # Darker to lighter

    # Convert the grayscale image to numpy array
    pixels = np.array(img)

    # Create ASCII art
    ascii_art = ''
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            ascii_art += get_ascii_char(pixels[i, j], ascii_chars)
        ascii_art += '\n'

    return ascii_art

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

def image_to_colored_ascii(image_path, grid_size, font_path, font_size):
    # Load the image
    img = Image.open(image_path)

    # Resize the image
    aspect_ratio = img.height / img.width
    new_width = grid_size
    new_height = int(aspect_ratio * new_width * 0.5)
    img = img.resize((new_width, new_height))

    # Convert image to grayscale for ASCII mapping
    gray_img = img.convert("L")

    # Create a new image for the colored ASCII art
    ascii_image = Image.new("RGB", img.size, color="black")
    draw = ImageDraw.Draw(ascii_image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Map each pixel to an ASCII character and color
    for i in range(img.height):
        for j in range(img.width):
            char = get_ascii_char(gray_img.getpixel((j, i)))
            color = img.getpixel((j, i))
            draw.text((j * font_size, i * font_size), char, fill=color, font=font)

    return ascii_image

# Path to the image file
image_path = 'svenfacecloseup.png'  # Replace with your image path
font_path = 'Industry-Demi.ttf'  # Replace with the path to a TrueType font

# Convert and print ASCII Art
# ascii_art = image_to_ascii(image_path, 120)
ascii_art_image = image_to_colored_ascii(image_path, 400, font_path, 6)
ascii_art_image.save('colored_ascii_art4.png')

# ascii_art2 = image_to_ascii_custom(image_path, 50, "svenra")

# print(ascii_art)
