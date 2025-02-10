import os
import random
import string
from PIL import Image, ImageDraw, ImageFont

os.makedirs('dataset_1', exist_ok=True)

font_paths = ['fonts\\font1.TTF','fonts\\font2.ttf'] 

def generate_random_word(length):
    word = ''.join(random.choices(string.ascii_lowercase, k=length))
    return ''.join(random.choice([char.upper(), char.lower()]) for char in word)

def create_noisy_background(size):
    background = Image.new('RGB', size, 'white')
    noise = Image.effect_noise(size, 100).convert('RGB')
    return Image.blend(background, noise, 0.2)

def create_captcha_image(text, font_paths, font_size=28):
    image = create_noisy_background((128, 32))
    draw = ImageDraw.Draw(image)
    
    valid_font_paths = [fp for fp in font_paths if os.path.exists(fp)]
    if valid_font_paths:
        font_path = random.choice(valid_font_paths)
    else:
        font_path = ImageFont.load_default()
    
    if isinstance(font_path, str):
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = font_path 
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((128 - text_width) // 2, (32 - text_height) // 2)
    
    draw.text(position, text, fill='black', font=font)
    
    return image

for i in range(35000):  
    print(i)
    word_length = random.randint(4, 8)  
    captcha_text = generate_random_word(word_length)
    captcha_image = create_captcha_image(captcha_text, font_paths)
    captcha_image.save(f'dataset_1/{captcha_text}.png')