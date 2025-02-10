import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

os.makedirs('dataset_0', exist_ok=True)

def generate_random_word(length):
    word = ''.join(random.choices(string.ascii_lowercase, k=length))
    return word.capitalize()

def create_captcha_image(text, font_path='calibri.ttf', font_size=20):
    image = Image.new('RGB', (128, 32), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((128 - text_width) // 2, (32 - text_height) // 2)  
    
    draw.text(position, text, fill='black', font=font)
    
    return image

for i in range(10):
    print(i)
    word_length = random.randint(4, 8)
    captcha_text = generate_random_word(word_length)
    captcha_image = create_captcha_image(captcha_text)
    captcha_image.save(f'dataset_test/{captcha_text}.png')