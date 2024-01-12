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

def generate_animated_ascii(image_path, grid_width, font_path, font_size, hidden_code, num_frames):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_width = grid_width * font_size
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height))
    font = ImageFont.truetype(font_path, font_size)
    ascii_chars = "@%#*+=-:. "  # Darker to lighter
    frames = []

    for _ in range(num_frames):
        frame = create_ascii_frame(img, font, ascii_chars, hidden_code)
        frames.append(frame)

    return frames

# Usage
image_path = 'svenra.png'
font_path = 'Industry-Demi.ttf'
frames = generate_animated_ascii(image_path, 150, font_path, 10, "svenra", 10)  # 10 frames


# Save as GIF
frames[0].save('animated_ascii.gif', save_all=True, append_images=frames[1:], loop=0, duration=100)
