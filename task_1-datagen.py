import os
import random
import string
from itertools import product
from PIL import Image, ImageDraw, ImageFont

# Constants
NUM_WORDS = 100
WORD_LENGTH_RANGE = (4, 8)
IMAGE_SIZE = (128, 32)
EASY_FONT_PATHS = ['arial.ttf', 'calibri.ttf', 'verdana.ttf', 'tahoma.ttf', 'georgia.ttf']  # Update these paths as needed
VARIED_FONT_PATHS = ['fonts/font1.TTF', 'fonts/font2.ttf']  # Update these paths as needed
EASY_IMAGES_PER_WORD = 5
MAX_HARD_IMAGES = 45
FONT_SIZE_EASY = 20
FONT_SIZE_HARD = 28

# Create main task directory
os.makedirs('task-1_data', exist_ok=True)

def generate_random_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_easy_image(text, font_path, font_size=FONT_SIZE_EASY):
    image = Image.new('RGB', IMAGE_SIZE, 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((IMAGE_SIZE[0] - text_width) // 2, (IMAGE_SIZE[1] - text_height) // 2)

    draw.text(position, text, fill='black', font=font)
    return image

def create_noisy_background(size):
    background = Image.new('RGB', size, 'white')
    noise = Image.effect_noise(size, 100).convert('RGB')
    return Image.blend(background, noise, 0.2)

def create_hard_image(text, font_path, font_size=FONT_SIZE_HARD):
    image = create_noisy_background(IMAGE_SIZE)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((IMAGE_SIZE[0] - text_width) // 2, (IMAGE_SIZE[1] - text_height) // 2)

    draw.text(position, text, fill='black', font=font)
    return image

# Generate 100 random words
words = [generate_random_word(random.randint(*WORD_LENGTH_RANGE)) for _ in range(NUM_WORDS)]

for word in words:
    # Create a separate directory for each word
    word_dir = os.path.join('task-1_data', word)
    os.makedirs(word_dir, exist_ok=True)

    # Create easy images
    for i in range(EASY_IMAGES_PER_WORD):
        easy_image = create_easy_image(word.capitalize(), EASY_FONT_PATHS[i % len(EASY_FONT_PATHS)])
        easy_image.save(os.path.join(word_dir, f'{word}_easy_{i+1}.png'))

    # Create hard images
    # Generate all capitalization permutations
    length = len(word)
    permutations = list(product([0, 1], repeat=length))
    hard_image_count = 0

    for caps in permutations:
        if hard_image_count >= MAX_HARD_IMAGES:
            break

        # Apply capitalization pattern
        hard_word = ''.join(
            char.upper() if caps[i] else char.lower() for i, char in enumerate(word)
        )

        for font_path in VARIED_FONT_PATHS:
            if hard_image_count >= MAX_HARD_IMAGES:
                break
            hard_image = create_hard_image(hard_word, font_path)
            hard_image.save(os.path.join(word_dir, f'{word}_hard_{hard_image_count + 1}.png'))
            hard_image_count += 1
