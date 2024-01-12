from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random

def map_char_to_intensity(char):
    """
    Simple heuristic to map a character to a grayscale intensity.
    This needs to be adjusted based on the characters used and desired effect.
    """
    return sum(ord(c) for c in char) % 256

# def get_ascii_char(value, ascii_chars):
#     """
#     Map a grayscale value to an ASCII character.
#     """
#     return ascii_chars[int(value / 256 * len(ascii_chars))]


def get_ascii_char(value, ascii_chars):
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

def image_to_colored_ascii(image_path, grid_width, font_path, font_size):
    # Load the image
    img = Image.open(image_path)

    # Calculate the new height of the image based on the aspect ratio
    aspect_ratio = img.height / img.width
    new_width = grid_width * font_size  # New width in pixels
    new_height = int(aspect_ratio * new_width)

    # Resize the image
    img = img.resize((new_width, new_height))

    # Convert image to grayscale for ASCII mapping
    gray_img = img.convert("L")

    # Create a new image for the colored ASCII art
    ascii_image = Image.new("RGB", img.size, color="black")
    draw = ImageDraw.Draw(ascii_image)

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Map each pixel to an ASCII character and color
    for i in range(0, img.height, font_size):
        for j in range(0, img.width, font_size):
            pixel_x, pixel_y = j, i
            char = get_ascii_char(gray_img.getpixel((pixel_x, pixel_y)))
            color = img.getpixel((pixel_x, pixel_y))
            draw.text((j, i), char, fill=color, font=font)

    return ascii_image

def image_to_colored_ascii_with_code(image_path, grid_width, font_path, font_size, hidden_code):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_width = grid_width * font_size
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height))
    gray_img = img.convert("L")
    ascii_image = Image.new("RGB", img.size, color="black")
    draw = ImageDraw.Draw(ascii_image)
    font = ImageFont.truetype(font_path, font_size)
    ascii_chars = "@%#*+=-:. "  # Darker to lighter

    code_index = 0
    for i in range(0, img.height, font_size):
        for j in range(0, img.width, font_size):
            if random.random() < 0.05:  # 5% chance to replace with hidden code
                char = hidden_code[code_index % len(hidden_code)]
                code_index += 1
            else:
                char = get_ascii_char(gray_img.getpixel((j, i)), ascii_chars)
            color = img.getpixel((j, i))
            draw.text((j, i), char, fill=color, font=font)

    return ascii_image


# Path to the image file
image_path = 'svenra.png'  # Replace with your image path
font_path = 'Industry-Demi.ttf'  # Replace with the path to a TrueType font
font_size = 10 

# Convert and print ASCII Art
# ascii_art = image_to_ascii(image_path, 120)
# ascii_art_image = image_to_colored_ascii(image_path, 200, font_path, font_size)
# ascii_art_image.save('colored_ascii_art6.png')
ascii_art_image = image_to_colored_ascii_with_code(image_path, 200, font_path, 10, "svenra")
ascii_art_image.save('colored_ascii_art_with_code.png')

# ascii_art2 = image_to_ascii_custom(image_path, 50, "svenra")

# print(ascii_art)
