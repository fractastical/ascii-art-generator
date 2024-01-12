from PIL import Image, ImageDraw, ImageFont, ImageSequence
import numpy as np
import random

def get_ascii_char(value, ascii_chars):
    return ascii_chars[int(value / 256 * len(ascii_chars))]

def create_ascii_frame(img, font, ascii_chars, hidden_code, probability=0.05):
    gray_img = img.convert("L")
    ascii_image = Image.new("RGB", img.size, color="black")
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

def generate_animated_ascii(image_path, grid_width, font_path, font_size, hidden_codes, num_frames_per_code):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_width = grid_width * font_size
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height))
    font = ImageFont.truetype(font_path, font_size)
    ascii_chars = "@%#*+=-:. "  # Darker to lighter
    frames = []

    for hidden_code in hidden_codes:
        for _ in range(num_frames_per_code):
            frame = create_ascii_frame(img, font, ascii_chars, hidden_code)
        frames.append(frame)

    return frames

image_path = 'svenra.png'
font_path = 'Industry-Demi.ttf'
hidden_codes = ["svenra", "(create(world"]
num_frames_per_code = 10 # Number of frames for each hidden code

frames = generate_animated_ascii(image_path, 150, font_path, 10, hidden_codes, num_frames_per_code)

frames[0].save('animated_ascii_phased.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)

