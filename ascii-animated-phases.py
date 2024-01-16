from PIL import Image, ImageDraw, ImageFont, ImageSequence
import numpy as np
import random


def get_ascii_char(value, ascii_chars):
    return ascii_chars[int(value / 256 * len(ascii_chars))]

def create_ascii_frame(img, font, ascii_chars, hidden_code, background_color, probability=0.05):
    gray_img = img.convert("L")
    ascii_image = Image.new("RGB", img.size, color=background_color)
    draw = ImageDraw.Draw(ascii_image)
    code_index = 0

    for i in range(0, img.height, font.size):
        for j in range(0, img.width, font.size):
            if random.random() < probability:
                char = hidden_code[code_index % len(hidden_code)]
                code_index += 1
            else:
                char = get_ascii_char(gray_img.getpixel((j, i)), ascii_chars)
            color = img.getpixel((j, i))
            draw.text((j, i), char, fill=color, font=font)

    return ascii_image


def generate_animated_ascii(image_path, grid_width, font_path, font_size, hidden_codes, num_frames_per_code, background_color):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_width = grid_width * font_size
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height))
    font = ImageFont.truetype(font_path, font_size)
    ascii_chars = ".*#%@"[::-1]  # Lighter to darker
    frames = []

    for hidden_code in hidden_codes:
        for _ in range(num_frames_per_code):
            frame = create_ascii_frame(img, font, ascii_chars, hidden_code, background_color)
            frames.append(frame)

    return frames

def read_hidden_codes(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Usage
hidden_codes_file_path = 'hidden_codes.txt'
hidden_codes = read_hidden_codes(hidden_codes_file_path)

image_path = 'waking_up.JPEG'
font_path = 'Industry-Demi.ttf'
num_frames_per_code = 10 # Number of frames for each hidden code
background_color = (207, 159, 255)  # Light background (RGB)

frames = generate_animated_ascii(image_path, 150, font_path, 10, hidden_codes, num_frames_per_code, background_color)

frames[0].save('encoded_image.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)

